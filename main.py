import sys
from typing import List

from aeroplane_project.api_adapter import get_raw_data
from aeroplane_project.models.aeroplane import Aeroplane
from aeroplane_project.processing import process_planes


def main() -> None:
    """Основная функция программы."""
    try:
        raw_data: List[List] = get_raw_data("https://opensky-network.org/api/states/all")
    except RuntimeError as exc:
        print(f"Ошибка API: {exc}")
        sys.exit(1)

    try:
        country_input: str = input("Введите страну для фильтрации: ").strip()

        top_n_input: str = input("Введите количество самолетов для топ N: ").strip()
        top_n: int = int(top_n_input)

        countries_input: str = input(
            "Фильтр по странам (через пробел, оставьте пустым для всех): "
        ).strip()
        countries: List[str] = countries_input.split() if countries_input else [country_input]

        alt_range_input: str = input("Диапазон высот (min max): ").strip()
        alt_min_str, alt_max_str = alt_range_input.split()
        alt_min: float = float(alt_min_str)
        alt_max: float = float(alt_max_str)

    except (ValueError, IndexError):
        print("Ошибка ввода. Пожалуйста, введите числа корректно.")
        sys.exit(1)

    planes: List[Aeroplane] = process_planes(
        raw_data=raw_data,
        countries=countries,
        alt_min=alt_min,
        alt_max=alt_max,
        top_n=top_n,
    )

    if not planes:
        print("Нет самолетов для выбранных фильтров.")
        return

    for plane in planes:
        print(
            f"{plane.callsign} ({plane.country}) - "
            f"высота: {plane.altitude}, скорость: {plane.velocity}"
        )


if __name__ == "__main__":
    main()
