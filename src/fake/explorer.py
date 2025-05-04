from faker import Faker

from model.explorer import Explorer


faker = Faker()

_explorers = [
    Explorer(
        name=faker.name(),
        country=faker.country(),
        description=faker.text(max_nb_chars=160),
    )
    for _ in range(10)
]


def get_all() -> list[Explorer]:
    return _explorers


def get_one(name: str) -> Explorer:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None


def create(explorer: Explorer) -> Explorer:
    pass


def modify(explorer: Explorer) -> Explorer:
    pass


def replace(explorer: Explorer) -> Explorer:
    pass


def delete(name: str) -> bool:
    pass
