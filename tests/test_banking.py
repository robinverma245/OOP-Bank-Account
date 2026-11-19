
"""Tests for bank account and transactions."""

from datetime import datetime

from banking import Account, Transaction


def test_transaction_amount():
    """Check the transaction amount."""
    transaction = Transaction(100)
    assert transaction.amount == 100


def test_transaction_timestamp():
    """Check the automatic timestamp."""
    transaction = Transaction(100)
    assert isinstance(transaction.timestamp, datetime)


def test_custom_timestamp():
    """Check a supplied timestamp."""
    timestamp = datetime(2020, 1, 1)
    transaction = Transaction(100, timestamp)
    assert transaction.timestamp == timestamp


def test_transaction_repr():
    """Check the transaction representation."""
    transaction = Transaction(100, datetime(2020, 1, 1))
    expected = (
        "Transaction(100, "
        "datetime.fromisoformat('2020-01-01T00:00:00'))"
    )
    assert repr(transaction) == expected


def test_transaction_str():
    """Check the formatted transaction."""
    transaction = Transaction(1234.56, datetime(2019, 1, 1))
    assert str(transaction) == "2019-01-01: +1,234.56"


def test_empty_account():
    """Check a new account."""
    account = Account()
    assert not account.transactions
    assert account.get_balance() == 0


def test_deposit():
    """Check deposits create positive transactions."""
    account = Account()
    account.deposit(-100)
    assert len(account.transactions) == 1
    assert isinstance(account.transactions[0], Transaction)
    assert account.transactions[0].amount == 100


def test_withdraw():
    """Check withdrawals create negative transactions."""
    account = Account()
    account.withdraw(90)
    assert len(account.transactions) == 1
    assert isinstance(account.transactions[0], Transaction)
    assert account.transactions[0].amount == -90


def test_balance():
    """Check the balance after transactions."""
    account = Account()
    account.deposit(100)
    account.withdraw(90)
    account.deposit(10)
    assert account.get_balance() == 20
