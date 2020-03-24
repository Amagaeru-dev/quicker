#!/usr/bin/env python
# -*- coding: utf-8 -*-

from googletrans import Translator
import sys

"""翻訳をするための単純なAPIを提供するモジュール
'googletrans'を使っているから、急に使えなくなるかもしれない。
"""


def trans(text, lang="-ja"):
    """googletransを使って翻訳をする
    例：
    >>>trans(Hello, -ja)
    こんにちは
    """
    if not lang:
        raise ValueError("翻訳先の言語が指定されていません。")

    if not text:
        raise ValueError("翻訳するテキストがありません。")

    if lang in "-":
        # 'lang'から'-'を取り除く
        # コマンドのオプションの記法に対応させるため
        lang = lang.strip("-")

    trans = Translator()
    # 翻訳をする
    trs_text = trans.translate(text, dest=lang).text
    return trs_text

# 他の関数でもtrnas()を使えるようにする
trans_func = trans


def trans_stdin(lang):
    """標準入力を`trans()`に渡す
    TODO:外部の関数を呼び出せるようにする。
    """
    global trans_func

    trs_lines = ""

    for line in sys.stdin.readlines():
        trs_lines += trans_func(line, lang=lang)

    return trs_lines
