#!/usr/bin/env python
# -*- coding: utf-8 -*-

from translation import trans as tr

"""モジュールのdocstringを翻訳するモジュール"""

def trans_doc(func, lang):
    """docstringを'trans.trans'で指定した言語に翻訳して返す"""
    doc = func.__doc__
    trs_doc = tr(doc, lang=lang)
    

print(trans_doc('print', '-jp'))