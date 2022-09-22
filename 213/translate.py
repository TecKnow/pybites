import re

non_translate_re = re.compile(
    r"((?:<code>.*?</code>)|(?:<pre>.*?</pre>))", flags=re.DOTALL)


def fix_translation(org_text: str, trans_text: str) -> str:
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    untranslated_elements = non_translate_re.split(org_text)
    translated_elements = non_translate_re.split(trans_text)
    assert len(untranslated_elements) == len(translated_elements)
    res_list = list(translated_elements)
    res_list[1::2] = untranslated_elements[1::2]
    return ''.join(res_list)
