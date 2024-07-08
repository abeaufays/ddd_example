from bank_transfer_layers.domain.account import Account
from bank_transfer_layers.infrastructure.django_orm import models


class DjangoRepository:
    # Here we could have some "requires transaction" decorator
    def save(self, account: Account) -> None:
        models.AccountModel.objects.update_or_create(
            id=account.id,
            defaults={"balance": account.balance},
        )

    def get(self, account_id: str) -> Account:
        db_account = models.AccountModel.objects.get(id=account_id)
        return Account(id=db_account.id, balance=db_account.balance)
