#!/usr/bin/env python
# -*- coding: utf-8 -*-

import trans

"""モジュールのdocstringを翻訳するモジュール"""


def trans_doc(func, lang):
    """docstringを'trans.trans'で指定した言語に翻訳して返す"""
    doc = func.__doc__
    trs_doc = trans.trans(doc, lang=lang)
    return trs_doc
