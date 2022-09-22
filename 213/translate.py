import re

non_translate_re = re.compile(
    r"((?:<code>.*?</code>)|(?:<pre>.*?</pre>))", flags=re.DOTALL)


def fix_translation(org_text: str, trans_text: str) -> str:
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    res = str()
    untranslated_elements = non_translate_re.split(org_text)
    translated_elements = non_translate_re.split(trans_text)
    assert len(untranslated_elements) == len(translated_elements)
    for org, trans in zip(untranslated_elements, translated_elements):
        if org.startswith(("<pre>", "<code>")):
            res += org
        else:
            res += trans
    return res


if __name__ == "__main__":
    from pprint import pprint
    from test_translate import bite_15_en
    pprint(non_translate_re.split(bite_15_en))
