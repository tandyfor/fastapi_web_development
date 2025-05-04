from faker import Faker

from model.creature import Creature


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
    return None


def create(creature: Creature) -> Creature:
    _creatures.append(creature)
    return creature


def modify(creature: Creature) -> Creature:
    pass


def replace(creature: Creature) -> Creature:
    pass


def delete(name: str) -> bool:
    pass
