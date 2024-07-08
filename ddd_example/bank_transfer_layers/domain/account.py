import attrs

from bank_transfer_layers.domain.abstract import UnitOfWork


@attrs.define
class Account:
    """
    Entity representing a bank account.
    """

    id: str
    balance: int

    def debit(self, amount: int, unit_of_work: UnitOfWork):
        if amount < 0:
            raise ValueError("Can't debit negative amount")
        if self.balance - amount < 0:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        unit_of_work.add(self)

    def credit(self, amount: int, unit_of_work: UnitOfWork):
        if amount < 0:
            raise ValueError("Can't credit negative amount")
        self.balance += amount
        unit_of_work.add(self)
