import pytest
from string_utils import StringUtils


def test_capitilize_success():
    string = StringUtils()
    res = string.capitilize('word')
    assert res == 'Word'

def test_capitilize_raises_wrong_variable_type_error():
    string = StringUtils()

    with pytest.raises(AttributeError):
        string.capitilize(1)

@pytest.mark.parametrize('word', ["", "apple"])
def test_trim(word):
    string = StringUtils()
    res = string.trim(50 * ' ' + word)
    assert res == word

def test_to_list_success():
    string = StringUtils()
    res = string.to_list("ab,cd,ef,gh")
    assert res == ["ab", "cd", "ef", "gh"]

def test_to_list_is_empty():
    string = StringUtils()
    res = string.to_list("")
    assert res == []

@pytest.mark.parametrize ('word, symbol', [("Apple", "pp"), ("House", "b")])
def test_contains(word, symbol):
    string = StringUtils()
    res = string.contains(string=word, symbol=symbol)
    assert res == (symbol in word)

@pytest.mark.parametrize ('word, symbol', [("apple", "a"), ("apple", "e"), ("apple", "w")])
def test_delete_symbol(word, symbol):
    string = StringUtils()
    word_length = len(word)
    symbol_in_word_count = word.count(symbol)
    res = string.delete_symbol(word, symbol)
    assert len(res) == word_length - symbol_in_word_count

@pytest.mark.parametrize ('word, symbol', [("apple", "a"), ("apple", "e")])
def test_starts_with_success(word, symbol):
    string = StringUtils()
    res = string.starts_with(string=word, symbol=symbol)
    assert res == (word[0] == symbol)

@pytest.mark.parametrize ('word, symbol', [("apple", "e"), ("apple", "a")])
def test_end_with(word, symbol):
    string = StringUtils()
    res = string.end_with(string=word, symbol=symbol)
    assert res == (word[-1] == symbol)

@pytest.mark.parametrize('word', ["", "apple"])
def test_is_empty(word):
    string = StringUtils()
    is_empty = True if not len(word) else False
    assert string.is_empty(word) == is_empty

@pytest.mark.parametrize ('lst', [[]])
def test_list_to_string_empty(lst):
    string = StringUtils()
    res = string.list_to_string(lst)

    assert len(res) == 0
    assert res == ""

@pytest.mark.parametrize ('lst', [[1, 2, 3], ["q", "w", "e", "r", "t", "y"]])
def test_list_to_string_not_empty(lst):
    string = StringUtils()
    res = string.list_to_string(lst)

    lst_count = len(lst)
    assert len(res) == lst_count + (lst_count - 1) * 2
    assert res == ", ".join([str(el) for el in lst])

@pytest.mark.parametrize ('lst', [[1, 2, 3], ["q", "w", "e", "r", "t", "y"]])
def test_list_to_string_custom_joiner(lst):
    string = StringUtils()
    joiner = " , "
    res = string.list_to_string(lst=lst, joiner=joiner)

    joiner_count = len(joiner)
    lst_count = len(lst)
    assert len(res) == lst_count + (lst_count - 1) * joiner_count
    assert res == joiner.join([str(el) for el in lst])










