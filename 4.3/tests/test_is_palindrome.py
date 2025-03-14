from main1 import is_palindrome
import pytest


@pytest.mark.parametrize("data, ex_result",
                         [
                             ("None enoN", True),
                             ("321", False),
                             ("321123", True),
                             (" ", True)
                         ])

def test_palindrome_positive(data, ex_result):
    assert is_palindrome(data) == ex_result


@pytest.mark.parametrize("data, ex_result",
                         [
                             (None, TypeError),
                             (123321, TypeError),
                             (0.1110, TypeError),
                             (["1", "2", "1"], TypeError),
                             (0, TypeError),
                             ("", ValueError)
                         ])

def test_palindrome_negative(data, ex_result):
    with pytest.raises(ex_result):
        is_palindrome(data)


@pytest.mark.parametrize("data, ex_result",
                         [
                             ("1", True)
                         ])

def test_palindrome_gran(data, ex_result):
    assert is_palindrome(data) == ex_result