from main1 import BankAccount
import pytest

@pytest.mark.parametrize("data, ex_result",
                         [
                             (1, 1),
                             (0.111111111111111111111111111111111111111111111, 0.1111111111111111),
                             (111, 111),
                             (1 + 20, 21),
                             (0 + 0.111111, 0.111111)
                         ])

def test_bank_account_deposit_positive(data, ex_result):
    account = BankAccount()

    account.deposit(data)
    assert account.get_balance() == ex_result


@pytest.mark.parametrize("data, ex_result",
                         [
                             ("111", TypeError),
                             ([[1], 2], TypeError),
                             ("[12]", TypeError),
                             (None, TypeError),
                             ("None", TypeError)
                         ])

def test_bank_account_deposit_negative(data, ex_result):
    account = BankAccount()

    with pytest.raises(ex_result):
        account.deposit(data)


@pytest.mark.parametrize("data, ex_result",
                         [
                             (1, -1),
                             (0.11, -0.11),
                             (0, 0)
                         ])

def test_bank_account_withdraw_positive(data, ex_result):
    account = BankAccount()

    account.withdraw(data)
    assert account.get_balance() == ex_result


@pytest.mark.parametrize("data, ex_result",
                         [
                             (0, ValueError),
                             ([[1], 2], TypeError),
                             ("", TypeError),
                             ([1], TypeError),
                             (None, TypeError)
                         ])

def test_bank_account_withdraw_negative(data, ex_result):
    account = BankAccount()

    with pytest.raises(ex_result):
        account.deposit(data)