from main import DiscountCalculator
import pytest


@pytest.fixture(scope="function")
def discount_calculator_fixture_data():

    calculator = DiscountCalculator()

    return calculator


@pytest.mark.calculator
@pytest.mark.parametrize("data1, data2, ex_result",
                         [
                             (100, 12, 88.0),
                             (1000, 12, 880.0),
                             (0.1, 12, 0.08800000000000001)
                         ])

def test_apply_discount_positive(discount_calculator_fixture_data, data1, data2, ex_result):

    assert discount_calculator_fixture_data.apply_discount(data1, data2) == ex_result



@pytest.mark.calculator
@pytest.mark.parametrize("data1, data2, ex_result",
                         [
                             (12, None, TypeError),
                             ([1], [2], TypeError),
                             (-100, 12, ValueError),
                             (100, -12, TypeError)
                         ])

def test_apply_discount_negative(discount_calculator_fixture_data, data1, data2, ex_result):

    with pytest.raises(ex_result):
        discount_calculator_fixture_data.apply_discount(data1, ex_result)