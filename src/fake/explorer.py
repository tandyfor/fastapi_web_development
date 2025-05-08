from faker import Faker

from model.explorer import Explorer
from errors import Duplicate, Missing


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
    raise Missing(msg=f"Missing {name}")


def contain(explorer: Explorer) -> bool | None:
    for _explorer in _explorers:
        if _explorer == explorer:
            return True


def create(explorer: Explorer) -> Explorer:
    if contain(explorer):
        raise Duplicate(msg=f"Duplicate {explorer.name} alrady exist.")
    _explorers.append(explorer)
    return explorer


def modify(name: str, explorer: Explorer) -> Explorer:
    for _explorer in _explorers:
        if _explorer.name == name:
            _explorer = explorer
            return explorer
    raise Missing(msg=f"Missing {name}")

def replace(explorer: Explorer) -> Explorer:
    pass


def delete(name: str) -> bool:
    for _explorer in _explorers:
        if _explorer.name == name:
            del _explorer
            return None
    raise Missing(msg=f"Missing {name}")
