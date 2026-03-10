import pytest

from aeroplane_project.models.aeroplane import Aeroplane
from aeroplane_project.utils.helpers import (
    filter_aeroplanes,
    get_aeroplanes_by_altitude,
    get_top_aeroplanes,
    sort_aeroplanes,
)


@pytest.fixture
def sample_planes():
    return [
        Aeroplane("AA101", "USA", 250.0, 10000.0),
        Aeroplane("BA202", "UK", 260.0, 12000.0),
        Aeroplane("CA303", "China", 240.0, 8000.0),
        Aeroplane("DA404", "USA", 270.0, 15000.0),
    ]


def test_from_raw():
    raw = ["icao24", "TEST1", "France", 0, 0, 0, 0, 11000, False, 230.5, 0, 0, 0]
    plane = Aeroplane.from_raw(raw)
    assert plane.callsign == "TEST1"
    assert plane.country == "France"
    assert plane.baro_altitude == 11000
    assert plane.velocity == 230.5


def test_filter_aeroplanes(sample_planes):
    filtered = filter_aeroplanes(sample_planes, ["USA"])
    assert len(filtered) == 2
    assert all(p.country == "USA" for p in filtered)


def test_get_aeroplanes_by_altitude(sample_planes):
    ranged = get_aeroplanes_by_altitude(sample_planes, (9000, 13000))
    assert len(ranged) == 2
    assert all(9000 <= p.baro_altitude <= 13000 for p in ranged)


def test_sort_aeroplanes(sample_planes):
    sorted_planes = sort_aeroplanes(sample_planes)
    assert sorted_planes[0].baro_altitude == 15000
    assert sorted_planes[-1].baro_altitude == 8000


def test_get_top_aeroplanes(sample_planes):
    sorted_planes = sort_aeroplanes(sample_planes)
    top_planes = get_top_aeroplanes(sorted_planes, 2)
    assert len(top_planes) == 2
    assert top_planes[0].baro_altitude >= top_planes[1].baro_altitude
