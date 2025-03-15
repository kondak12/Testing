from main import BankAccount
import pytest


@pytest.fixture(scope="function")
def bank_fixture_data():

    return BankAccount()


@pytest.mark.bank_account
@pytest.mark.parametrize("data, ex_result",
                         [
                             (1, 1),
                             (1234567890, 1234567890),
                             (0.11, 0.11),
                             (0, 0)
                         ])
def test_deposit_positive(bank_fixture_data, data, ex_result):
    bank_fixture_data.balance = 0

    assert bank_fixture_data.deposit(data) == ex_result



@pytest.mark.bank_account
@pytest.mark.parametrize("data, ex_result",
                         [
                             ("", TypeError),
                             (None, TypeError),
                             ([], TypeError),
                             (-1, ValueError),
                             ([-1], TypeError)
                         ])
def test_deposit_negative(bank_fixture_data, data, ex_result):
    bank_fixture_data.balance = 0

    with pytest.raises(ex_result):
        bank_fixture_data.deposit(data)



@pytest.mark.bank_account
@pytest.mark.parametrize("data, ex_result",
                         [
                             (100, 0),
                             (0.11, 99.89)
                         ])
def test_withdraw_positive(bank_fixture_data, data, ex_result):
    bank_fixture_data.balance = 100

    assert bank_fixture_data.withdraw(data) == ex_result



@pytest.mark.bank_account
@pytest.mark.parametrize("data, ex_result",
                         [
                             ("", TypeError),
                             (None, TypeError),
                             (-1, ValueError),
                             ([-1], TypeError),
                             (1, ValueError)
                         ])
def test_withdraw_negative(bank_fixture_data, data, ex_result):

    with pytest.raises(ex_result):
        bank_fixture_data.withdraw(data)