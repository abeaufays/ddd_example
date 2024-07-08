from bank_transfer_layers.domain.abstract import UnitOfWork
from .account import Account


def transfer(
    from_account: Account, to_account: Account, amount: int, unit_of_work: UnitOfWork
):
    """
    Service to transfer funds between accounts.
    """
    try:
        from_account.debit(amount, unit_of_work)
        to_account.credit(amount, unit_of_work)
    except ValueError as e:
        raise ValueError("Transfer failed") from e
