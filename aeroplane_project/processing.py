from typing import List

from aeroplane_project.models.aeroplane import Aeroplane


def process_planes(
    raw_data: List[List],
    countries: List[str],
    alt_min: float,
    alt_max: float,
    top_n: int,
) -> List[Aeroplane]:
    """Фильтрует и возвращает список самолетов."""
    result: List[Aeroplane] = []

    for row in raw_data:
        if len(row) < 10:
            continue

        callsign = row[1]
        country = row[2]
        altitude = row[7]
        velocity = row[9]

        if callsign is None or country is None:
            continue

        if country not in countries:
            continue

        if altitude is None or not (alt_min <= float(altitude) <= alt_max):
            continue

        result.append(
            Aeroplane(
                callsign=str(callsign).strip(),
                country=str(country),
                altitude=float(altitude),
                velocity=float(velocity) if velocity is not None else 0.0,
            )
        )

    return result[:top_n]
