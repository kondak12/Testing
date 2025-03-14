from main1 import Library
import pytest


@pytest.mark.parametrize("data, ex_result",
                         [
                             ("Book A", True),
                             ("\033[31m", True),
                             ("123", True)
                         ])


def test_add_book_positive(data, ex_result):
    library = Library()

    library.add_book(data)
    assert library.find_book(data) == ex_result



@pytest.mark.parametrize("data, ex_result",
                         [
                             ("   ", KeyError),
                             ([[1], 2], TypeError),
                             ("", KeyError),
                             (None, AttributeError),
                             (123, AttributeError)
                         ])

def test_add_book_negative(data, ex_result):
    library = Library()

    with pytest.raises(ex_result):
        library.add_book(data)




@pytest.mark.parametrize("data1, data2, ex_result1, ex_result2",
                         [
                             ("Book A", "Book B", True, False),
                             ("123", "\033[31m", True, False),
                             ("a", "a", True, False)
                         ])



def test_remove_book_positive(data1, data2, ex_result1, ex_result2):
    library = Library()

    library.add_book(data1)
    library.add_book(data2)

    assert library.find_book(data1) == ex_result1
    assert library.find_book(data2) == ex_result1

    library.remove_book(data1)
    library.remove_book(data2)

    assert library.find_book(data1) == ex_result2
    assert library.find_book(data2) == ex_result2