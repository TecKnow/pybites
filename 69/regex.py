import re
import string


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    return re.search(r"\b\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\b", text)


def is_integer(number):
    """Return True if number is an integer"""
    return re.fullmatch(r"-?\d+", str(number))


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    return re.search(r"\w-\w", text)


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    paren_re = re.compile(r"(.*?)\s*?\(.*?\)\s*?(.*?)$")
    repl_pattern_str = r"\g<1>\g<2>"
    current_str = text
    while (reduced_str := paren_re.sub(repl_pattern_str, current_str)) != current_str:
        current_str = reduced_str
    return current_str


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    return [m for m in re.split(rf"[{string.punctuation}]\s*", text) if m]


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    return re.sub(r"[ ][ ]+", " ", text)


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    return re.search(r"[aeiou]{3}", word)


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    return re.sub(r"(?P<d>\d\d)/(?P<m>\d\d)/(?P<y>\d\d\d\d)", r"\g<m>/\g<d>/\g<y>", date)


if __name__ == "__main__":
    print(remove_duplicate_spacing('This is a   string with  too    much spacing'))
