from collections import Counter


def calculate_gc_content(sequence: str) -> float:
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    character_frequencies = Counter(sequence.casefold())
    a_count = character_frequencies["a"]
    c_count = character_frequencies["c"]
    g_count = character_frequencies["g"]
    t_count = character_frequencies["t"]
    total_bases = sum((a_count, c_count, g_count, t_count))
    gc_bases = sum((g_count, c_count))
    gc_ratio = gc_bases/total_bases
    gc_content = gc_ratio * 100
    return round(gc_content, 2)
