from bbquote.lib import get_quote


def test_quote_len():
    assert len(get_quote()) != 0
