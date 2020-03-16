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


def input_stdin(lang):
    """標準入力を`trans()`に渡す
    TODO:外部の関数を呼び出せるようにする。
    """

    def inner_trans(text, lang=lang):
        """input_stdin()内のtrans()
        引数はtrans()の時から、'text'を除いただけ。
        """
        lang = lang.strip("-")
        trans = Translator()
        # 翻訳をする メソッドチェーンでよいかどうかはまた考える。
        return trans.translate(text, dest=lang).text

    trs_lines = ''

    for line in sys.stdin.readlines():
        trs_lines += inner_trans(line, lang=lang)
        
    return trs_lines             


