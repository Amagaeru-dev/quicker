from translation import trans


def test_trans():
    """trans.trans()のテストをする。"""
    text = "Hello"
    assert trans.trans(text=text, lang="-ja")
