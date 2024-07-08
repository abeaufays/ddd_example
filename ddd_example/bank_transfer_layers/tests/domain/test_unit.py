import pytest
from bank_transfer_layers.domain.account import Account
from bank_transfer_layers.domain.transfer import transfer
from bank_transfer_layers.domain.abstract import UnitOfWork


class FakeUnitOfWork:
    def __init__(self): self.repository = None
    def __enter__(self) -> UnitOfWork: return self
    def __exit__(self, *args): pass
    def add(self, account: Account) -> None: pass
    def commit(self) -> None: pass
    def rollback(self) -> None: pass


class TestAccountDebit:
    def test_account_debit_ok(self):
        account = Account(id="1", balance=100)
        with FakeUnitOfWork() as uow:
            account.debit(50, uow)
        assert account.balance == 50

    def test_account_debit_insufficient_funds(self):
        account = Account(id="1", balance=40)
        with pytest.raises(ValueError):
            with FakeUnitOfWork() as uow:
                account.debit(50, uow)
        assert account.balance == 40

    def test_account_debit_negative_amount(self):
        account = Account(id="1", balance=100)
        with pytest.raises(ValueError):
            with FakeUnitOfWork() as uow:
                account.debit(-20, uow)
        assert account.balance == 100
class TestAccountCredit:
    def test_account_credit_ok(self):
        account = Account(id="1", balance=100)
        with FakeUnitOfWork() as uow:
            account.credit(50, uow)
        assert account.balance == 150
    
    def test_account_credit_negative_amount(self):
        account = Account(id="1", balance=100)
        with pytest.raises(ValueError):
            with FakeUnitOfWork() as uow:
                account.credit(-20, uow)
        assert account.balance == 100

class TestTransfer:
    def test_transfer_ok(self):
        from_account = Account(id="1", balance=100)
        to_account = Account(id="2", balance=100)
        with FakeUnitOfWork() as uow:
            transfer(from_account, to_account, 50, uow)
        assert from_account.balance == 50
        assert to_account.balance == 150
    
    def test_transfer_insufficient_funds(self):
        from_account = Account(id="1", balance=40)
        to_account = Account(id="2", balance=100)
        with pytest.raises(ValueError):
            with FakeUnitOfWork() as uow:
                transfer(from_account, to_account, 50, uow)
        assert from_account.balance == 40
        assert to_account.balance == 100