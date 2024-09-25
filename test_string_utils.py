from string_utils import StringUtils

def test_capitalize():
    string = StringUtils()
    res = string.capitalize('word')
    assert res == 'Word'

def test_trim():
    string = StringUtils()
    whitespace = " "
    while (string.startswith(whitespace)):
        string = string.removeprefix(whitespace)
        res = string(' word')
        assert res == 'word'



