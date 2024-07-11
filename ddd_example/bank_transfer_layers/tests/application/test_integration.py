from bank_transfer_layers.application.use_case import transfer_fund
from bank_transfer_layers.application.config import get_repository
from bank_transfer_layers.domain.account import Account

import pytest


@pytest.mark.django_db(transaction=True)
def test_transfer_funds_ok():
    # Given 
    repository = get_repository()

    repository.save(Account("1", 100))
    repository.save(Account("2", 100))

    # When 
    transfer_fund("1", "2", 50)

    # Then
    assert repository.get("1").balance == 50
    assert repository.get("2").balance == 150