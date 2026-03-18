from dataclasses import dataclass


@dataclass
class Aeroplane:
    callsign: str
    country: str
    altitude: float
    velocity: float
