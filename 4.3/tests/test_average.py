from main1 import average
import pytest


@pytest.mark.parametrize("data, ex_result",
                         [
                             ([12 + 12, 0.111111111], 12.0555555555),
                             ([32112343523141435], 3.2112343523141436e+16),
                             ([1, 3, 3.14], 2.3800000000000003)
                         ])

def test_average_positive(data, ex_result):
    assert average(data) == ex_result


@pytest.mark.parametrize("data, ex_result",
                         [
                             ([None], TypeError),
                             (123321, TypeError),
                             ([0.1110, "", "1", "<"], TypeError),
                             ([[0], [0], [1]], TypeError),
                             ("['0', '1']", TypeError)
                         ])

def test_average_negative(data, ex_result):
    with pytest.raises(ex_result):
        average(data)


@pytest.mark.parametrize("data, ex_result",
                         [
                             ([1245246357463452341235463253412352461], 1.2452463574634523e+36)
                         ])

def test_average_gran(data, ex_result):
    assert average(data) == ex_result