#!/usr/bin/env python
# -*- coding: utf-8 -*-

from googletrans import Translator
import sys

"""翻訳をするための単純なAPIを提供するモジュール
'googletrans'を使っているから、急に使えなくなるかもしれない。
"""


def tarns(text, lang="-ja"):
    """googletransを使って翻訳をする
    例：
    >>>trans(Hello, -ja)
    こんにちは
    """
    # 'lang'から'-'を取り除く
    # コマンドのオプションの記法に対応させるため
    lang = lang.strip("-")
    trans = Translator()
    # 翻訳をする メソッドチェーンでよいかどうかはまた考える。
    return trans.translate(text, dest=lang).text

def input_stdin(lang='ja'):
    """標準入力を`trans()`に渡す"""
    trs_lines = None
    for line in sys.stdin:
        print(trans(line, lang=lang))

input_stdin()