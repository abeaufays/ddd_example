from __future__ import annotations
from django.db import transaction

from bank_transfer_layers.domain.account import Account
from bank_transfer_layers.infrastructure.django_orm.repository import (
    DjangoRepository,
)
from bank_transfer_layers.domain.abstract import Repository, UnitOfWork


class DjangoUnitOfWork:
    def __enter__(self) -> UnitOfWork:
        self.repository: Repository = DjangoRepository()
        transaction.set_autocommit(False)
        return self

    def __exit__(self, *args):
        self.rollback()
        transaction.set_autocommit(True)

    def add(self, account: Account) -> None:
        self.repository.save(account)

    def commit(self) -> None:
        transaction.commit()

    def rollback(self) -> None:
        
        transaction.rollback()
