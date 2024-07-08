from __future__ import annotations
from typing import Protocol

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bank_transfer_layers.domain.account import Account


class Repository(Protocol):
    def save(self, account: Account) -> None:
        """
        Update or save an account.
        Should not be used outside of a unit of work.
        """

    def get(self, account_id: str) -> Account:
        """
        Retrieve an account by its id.
        """


class UnitOfWork(Protocol):
    repository: Repository

    def __enter__(self) -> UnitOfWork: ...
    def __exit__(self, *args): ...
    def add(self, account: Account) -> None: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
