from string_utils import StringUtils

def test_capitilize():
    string = StringUtils()
    res = string.capitilize('word')
    assert res == 'Word'

def test_trim():
    string = StringUtils()
    whitespace = " "
    while (string.startswith(whitespace)):
        string = string.removeprefix(whitespace)
        res = string(' word')
        assert res == 'word'



