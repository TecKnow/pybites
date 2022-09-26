import os
from typing import Dict, List, Optional, NamedTuple, Sequence
from urllib.request import urlretrieve
from typing import Counter
import logging

logging.basicConfig()

logger = logging.getLogger(__name__)

# Translation Table:
# https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG11
# Each column represents one entry. Codon = {Base1}{Base2}{Base3}
# All Base 'T's need to be converted to 'U's to convert DNA to RNA
TRANSL_TABLE_11 = """
    AAs  = FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG
  Starts = ---M------**--*----M------------MMMM---------------M------------
  Base1  = TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG
  Base2  = TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG
  Base3  = TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG
"""

# Converted from http://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Staphylococcus_aureus_Newman_uid58839/NC_009641.ffn  # noqa E501
URL = "https://bites-data.s3.us-east-2.amazonaws.com/NC_009641.txt"

# Order of bases in the table
BASE_ORDER = ["U", "C", "A", "G"]


class TableEntry(NamedTuple):
    codon: str
    amino_acid_letter: str
    frequency_per_1000: float
    absolute_occurances: int

    def __str__(self) -> str:
        return f"{self.codon}:  {self.amino_acid_letter}   {self.frequency_per_1000:>4}  {self.absolute_occurances:>5}"


def _preload_sequences(url=URL):
    """
    Provided helper function
    Returns coding sequences, one sequence each line
    """
    filename = os.path.join(os.getenv("TMP", "/tmp"), "NC_009641.txt")
    if not os.path.isfile(filename):
        urlretrieve(url, filename)
    with open(filename, "r") as f:
        return f.readlines()


def _parse_coding_sequence(trans_table: Dict[str, str], coding_sequence: str) -> Optional[Dict[str, int]]:
    res_dict: Dict[str, int] = dict()
    coding_sequence = coding_sequence.strip()
    logger.debug(coding_sequence)
    for codon in (found_codon for i in range(0, len(coding_sequence), 3) if (found_codon := coding_sequence[i:i+3])):
        if codon not in trans_table.keys():
            logger.debug(f"Found non coding sequence \"{codon}\"")
            return None
        res_dict[codon] = res_dict.get(codon, 0) + 1
    return res_dict


def _parse_trans_table(trans_table: str = TRANSL_TABLE_11) -> Dict[str, str]:
    trans_table_lines = [line for line in trans_table.splitlines() if line]
    trans_table_lines_data = [line.split(
        "=")[1].strip() for line in trans_table_lines]
    trans_table_lines_data[-3:] = [line.replace("T", "U")
                                   for line in trans_table_lines_data[-3:]]
    zip_list = list(zip(*trans_table_lines_data))
    pivot_table = [(''.join((B1, B2, B3)), AA)
                   for AA, *_, B1, B2, B3 in zip_list]
    return dict(pivot_table)


def _calculate_stats(sequences: Sequence[str], translation_table_str: str) -> List[TableEntry]:
    trans_dict = _parse_trans_table(translation_table_str)
    res_counter: Counter[str] = Counter()
    for seq in sequences:
        res_counter.update(_parse_coding_sequence(trans_dict, seq))
    total_codons = sum(res_counter.values())
    return sorted(
        [
            TableEntry(
                codon,
                trans_dict[codon],
                round(((count/total_codons)*1000), 1),
                count)
            for codon, count
            in res_counter.items()],
        key=lambda x: tuple(BASE_ORDER.index(c) for c in x.codon))


def _block_string(entries: Sequence[TableEntry], block_num: int = 0) -> str:
    return (
        f"|  {entries[block_num + 0]}  |  {entries[block_num + 4]}  |  {entries[block_num +  8]}  |  {entries[block_num + 12]}  |\n"
        f"|  {entries[block_num + 1]}  |  {entries[block_num + 5]}  |  {entries[block_num +  9]}  |  {entries[block_num + 13]}  |\n"
        f"|  {entries[block_num + 2]}  |  {entries[block_num + 6]}  |  {entries[block_num + 10]}  |  {entries[block_num + 14]}  |\n"
        f"|  {entries[block_num + 3]}  |  {entries[block_num + 7]}  |  {entries[block_num + 11]}  |  {entries[block_num + 15]}  |"
    )


def return_codon_usage_table(
    sequences: List[str] = _preload_sequences(), translation_table_str: str = TRANSL_TABLE_11
):
    """
    Receives a list of gene sequences and a translation table string
    Returns a string with all bases and their frequencies in a table
    with the following fields:
    codon_triplet: amino_acid_letter frequency_per_1000 absolute_occurrences

    Skip invalid coding sequences:
       --> must consist entirely of codons (3-base triplet)
    """
    HEADER = "|  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |  Codon AA  Freq  Count  |"
    DIVIDER = "---------------------------------------------------------------------------------------------------------"
    entries = _calculate_stats(sequences, translation_table_str)
    res_str = "\n".join([HEADER] + [DIVIDER] +
                        [_block_string(entries, i) + "\n" + DIVIDER for i in range(0, 64, 16)])
    return res_str


if __name__ == "__main__":
    print(return_codon_usage_table())
