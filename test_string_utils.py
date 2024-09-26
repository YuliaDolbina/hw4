import pytest
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
        res = string.trim(' word')
        assert res == 'word'

def test_to_list():
    string = StringUtils()
    res = string.to_list("ab,cd,ef,gh")
    assert res == ["ab", "cd", "ef", "gh"]

@pytest.mark.parametrize ('word, letter', [("Apple", "a"), ("House", "b")])
def test_contains(word, letter):
    string = StringUtils()
    res = string.contains(word, letter)
    assert res == False

@pytest.mark.parametrize ('word, symbol', [("apple", "a"), ("apple", "e")])
def test_delete_symbol(word, symbol):
    string = StringUtils()
    res = string.delete_symbol(word, symbol)
    assert res == res








