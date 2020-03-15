#!/usr/bin/env python
# -*- coding: utf-8 -*-

from googletrans import Translator

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
