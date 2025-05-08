import os

import pytest
from fastapi import HTTPException

os.environ["CRYPTID_UNIT_TEST"] = "true"
from model.explorer import Explorer
from web import explorer


@pytest.fixture
def sample() -> Explorer:
    return Explorer(
        name="Marco Polo",
        country="Italy",
        description="Famous Venetian merchant and explorer.",
    )


@pytest.fixture
def fakes() -> list[Explorer]:
    return explorer.get_all()


def assert_duplicate(exc):
    assert exc.value.status_code == 409
    assert "Duplicate" in exc.value.detail


def assert_missing(exc):
    assert exc.value.status_code == 404
    assert "Missing" in exc.value.detail


def test_create(sample):
    assert explorer.create(sample) == sample


def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as exc:
        explorer.create(fakes[0])
    assert_duplicate(exc)


def test_get_one(fakes):
    assert explorer.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        explorer.get_one("Unknown Explorer")
    assert_missing(exc)


def test_get_all(fakes):
    assert len(fakes) > 0


def test_modify(fakes):
    updated_explorer = Explorer(
        name=fakes[0].name,
        country="China",
        description="Updated description.",
    )
    assert explorer.modify(fakes[0].name, updated_explorer) == updated_explorer


def test_modify_missing(sample):
    with pytest.raises(HTTPException) as exc:
        explorer.modify("Unknown Explorer", sample)
    assert_missing(exc)


def test_delete(fakes):
    assert explorer.delete(fakes[0].name) is None


def test_delete_missing():
    with pytest.raises(HTTPException) as exc:
        explorer.delete("Unknown Explorer")
    assert_missing(exc)