from bank_transfer_layers.domain.abstract import (
    Repository,
    UnitOfWork,
)
from bank_transfer_layers.infrastructure.django_orm.repository import (
    DjangoRepository,
)
from bank_transfer_layers.infrastructure.django_orm.unit_of_work import (
    DjangoUnitOfWork,
)


def get_unit_of_work() -> UnitOfWork:
    return DjangoUnitOfWork()


def get_repository() -> Repository:
    return DjangoRepository()
