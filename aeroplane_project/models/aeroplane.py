from typing import Any


class Aeroplane:
    __slots__ = ("callsign", "country", "velocity", "baro_altitude")

    def __init__(
        self, callsign: str, country: str, velocity: float, baro_altitude: float
    ) -> None:
        self.callsign = callsign
        self.country = country
        self.velocity = velocity
        self.baro_altitude = baro_altitude

    @classmethod
    def from_raw(cls, raw_data: list[Any]) -> "Aeroplane":
        """
        Создаёт объект Aeroplane из списка raw_data, как возвращает OpenSky API
        raw_data = [
            "icao24", "callsign", "origin_country", time_position,
            last_contact, longitude, latitude, baro_altitude,
            on_ground, velocity, true_track, vertical_rate, ...
        ]
        """
        return cls(
            callsign=raw_data[1].strip() if raw_data[1] else "N/A",
            country=raw_data[2],
            velocity=float(raw_data[9]) if raw_data[9] else 0.0,
            baro_altitude=float(raw_data[7]) if raw_data[7] else 0.0,
        )

    def __repr__(self) -> str:
        return f"{self.callsign} | {self.country} | Высота: {self.baro_altitude} м | Скорость: {self.velocity} м/с"
