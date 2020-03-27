#!/usr/bin/env python
# -*- coding: utf-8 -*-

from googletrans import Translator
import sys

"""This module is modules to provide simple APi
This module can't use Because use googletrans.
This module may not be usable because it depends on googletrans.
"""


def trans(text, lang="-ja"):
    """Translation use to 'googletrans'
    例：
    >>>trans("Hello", -ja)
    こんにちは
    """
    if not lang:
        raise ValueError("Destination language not specified.")

    if not text:
        raise ValueError("No strings to translate")

    if lang in "-":
        # remove "-" from lang
        # To respond to command input
        lang = lang.strip("-")

    trans = Translator()
    # Do translation
    trs_text = trans.translate(text, dest=lang).text
    return trs_text


# # For use in other functions
trans_func = trans



