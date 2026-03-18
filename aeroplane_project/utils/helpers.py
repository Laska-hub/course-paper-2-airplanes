from typing import List

from aeroplane_project.models.aeroplane import Aeroplane


def filter_by_altitude(planes: List[Aeroplane], min_alt: float, max_alt: float) -> List[Aeroplane]:
    """Фильтрует самолеты по диапазону высоты."""
    return [plane for plane in planes if min_alt <= plane.altitude <= max_alt]


def filter_by_country(planes: List[Aeroplane], countries: List[str]) -> List[Aeroplane]:
    """Фильтрует самолеты по странам."""
    return [plane for plane in planes if plane.country in countries]
