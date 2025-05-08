import os

import pytest

os.environ["CRYPTID_UNIT_TEST"] = "true"
from model.explorer import Explorer
from errors import Missing, Duplicate
from service import explorer as service


@pytest.fixture
def sample() -> Explorer:
    return Explorer(
        name="Marco Polo",
        country="Italy",
        description="Famous Venetian merchant and explorer.",
    )


def test_create(sample):
    resp = service.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    # service.create(sample)
    with pytest.raises(Duplicate):
        service.create(sample)


def test_get_one(sample):
    # service.create(sample)
    resp = service.get_one(sample.name)
    assert resp == sample


def test_get_one_missing():
    with pytest.raises(Missing):
        service.get_one("Unknown Explorer")


def test_get_all(sample):
    # service.create(sample)
    resp = service.get_all()
    assert len(resp) > 0
    assert sample in resp


def test_modify(sample):
    # service.create(sample)
    updated_explorer = Explorer(
        name=sample.name,
        country="China",
        description="Updated description.",
    )
    resp = service.modify(sample.name, updated_explorer)
    assert resp == updated_explorer


def test_modify_missing(sample):
    with pytest.raises(Missing):
        service.modify("Unknown Explorer", sample)


def test_delete(sample):
    # service.create(sample)
    resp = service.delete(sample.name)
    assert resp is None


def test_delete_missing():
    with pytest.raises(Missing):
        service.delete("Unknown Explorer")