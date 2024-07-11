from bank_transfer_layers.domain.transfer import transfer
from . import config


def transfer_fund(from_account_id: str, to_account_id: str, amount: int) -> None:
    """
    Use case to transfer funds between accounts.

    :param str from_account_id: Id of the account that money comes from
    :param str to_account_id: Id of the account that money goes to
    :param int amount: Amount to transfer
    """
    repository = config.get_repository()

    with config.get_unit_of_work() as unit_of_work:
        from_account = repository.get(from_account_id)
        to_account = repository.get(to_account_id)

        transfer(from_account, to_account, amount, unit_of_work)

        unit_of_work.commit()
