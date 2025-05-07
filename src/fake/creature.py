from faker import Faker
from fastapi import HTTPException

from model.creature import Creature
from errors import Duplicate, Missing


faker = Faker()

_creatures = [
    Creature(
        name=faker.name(),
        aka=faker.name(),
        area=faker.country(),
        country=faker.country(),
        description=faker.text(max_nb_chars=160),
    )
    for _ in range(10)
]


def get_all() -> list[Creature]:
    return _creatures


def get_one(name: str) -> Creature:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    raise Missing(msg=f"Missing {name}")


def create(creature: Creature) -> Creature:
    if contain(creature):
        raise Duplicate(msg=f"Duplicate: creature {creature.name} alrady exist.")
    _creatures.append(creature)
    return creature


def modify(name: str, creature: Creature) -> Creature:
    for _creature in _creatures:
        if _creature.name == name:
            _creature = creature
            return creature
    raise Missing(msg=f"Missing")

def replace(creature: Creature) -> Creature:
    pass


def delete(name: str) -> bool:
    for _creature in _creatures:
        if _creature.name == name:
            del _creature
            return None
    raise Missing(msg=f"Missing")


def contain(creature: Creature) -> bool | None:
    for _creature in _creatures:
        if creature.name == _creature.name:
            return True