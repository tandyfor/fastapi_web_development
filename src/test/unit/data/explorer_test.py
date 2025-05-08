import os

import pytest

from model.explorer import Explorer
from errors import Missing, Duplicate


os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import explorer



@pytest.fixture
def sample() -> Explorer:
    return Explorer(
        name="Marco Polo",
        country="Italy",
        description="Famous Venetian merchant and explorer.",
    )


def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        explorer.create(sample)


def test_get_one(sample):
    # explorer.create(sample)
    resp = explorer.get_one(sample.name)
    assert resp == sample


def test_get_one_missing():
    with pytest.raises(Missing):
        explorer.get_one("Unknown Explorer")


def test_get_all(sample):
    resp = explorer.get_all()
    assert len(resp) > 0
    assert sample in resp


def test_modify(sample):
    updated_explorer = Explorer(
        name=sample.name,
        country="China",
        description="Updated description.",
    )
    resp = explorer.modify(sample.name, updated_explorer)
    assert resp == updated_explorer


def test_modify_missing(sample):
    with pytest.raises(Missing):
        explorer.modify("Unknown Explorer", sample)


def test_delete(sample):
    resp = explorer.delete(sample.name)
    assert resp is None


def test_delete_missing():
    with pytest.raises(Missing):
        explorer.delete("Unknown Explorer")