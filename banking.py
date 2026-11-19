
"""Bank account and transaction classes."""

from datetime import datetime


class Transaction:
    """Represent a bank account transaction."""

    def __init__(self, amount, timestamp=None):
        """Initialize the transaction."""
        self.amount = amount
        self.timestamp = (
            timestamp if timestamp is not None else datetime.now()
        )

    def __repr__(self):
        """Return a reproducible representation."""
        return (
            f"Transaction({self.amount!r}, "
            f"datetime.fromisoformat({self.timestamp.isoformat()!r}))"
        )

    def __str__(self):
        """Return the formatted transaction."""
        return (
            f"{self.timestamp:%Y-%m-%d}: "
            f"{self.amount:+,.2f}"
        )


class Account:
    """Represent a bank account."""

    def __init__(self):
        """Initialize an empty account."""
        self.transactions = []

    def deposit(self, amount):
        """Add a deposit transaction."""
        transaction = Transaction(abs(amount))
        self.transactions.append(transaction)

    def withdraw(self, amount):
        """Add a withdrawal transaction."""
        transaction = Transaction(-abs(amount))
        self.transactions.append(transaction)

    def get_balance(self):
        """Return the current account balance."""
        return sum(
            transaction.amount
            for transaction in self.transactions
        )
