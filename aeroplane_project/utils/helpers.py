from typing import List, Tuple

from aeroplane_project.models.aeroplane import Aeroplane


def filter_aeroplanes(planes: List[Aeroplane], countries: List[str]) -> List[Aeroplane]:
    return [p for p in planes if p.country in countries]


def get_aeroplanes_by_altitude(
    planes: List[Aeroplane], altitude_range: Tuple[float, float]
) -> List[Aeroplane]:
    min_alt, max_alt = altitude_range
    return [p for p in planes if min_alt <= p.baro_altitude <= max_alt]


def sort_aeroplanes(planes: List[Aeroplane]) -> List[Aeroplane]:
    return sorted(planes, key=lambda p: p.baro_altitude, reverse=True)


def get_top_aeroplanes(planes: List[Aeroplane], top_n: int) -> List[Aeroplane]:
    return planes[:top_n]
