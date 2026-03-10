from typing import List, Tuple

from aeroplane_project.api_adapter import AeroplanesAPI
from aeroplane_project.models.aeroplane import Aeroplane
from aeroplane_project.utils.helpers import (
    filter_aeroplanes,
    get_aeroplanes_by_altitude,
    get_top_aeroplanes,
    sort_aeroplanes,
)


def user_interaction() -> None:
    country = input("Введите название страны для запроса: ")
    top_n = int(input("Введите количество самолетов для топ N: "))
    filter_words = input(
        "Введите страны для фильтрации по регистрации (через пробел): "
    ).split()
    altitude_input = input(
        "Введите диапазон высот полета через дефис (например 10000-15000): "
    )

    # Парсим диапазон высот
    try:
        if "-" in altitude_input:
            min_alt, max_alt = map(float, altitude_input.split("-"))
        else:
            raise ValueError
    except ValueError:
        print("Некорректный формат диапазона высот. Используется 0-100000")
        min_alt, max_alt = 0, 100000

    altitude_range: Tuple[float, float] = (min_alt, max_alt)

    api = AeroplanesAPI()
    raw_data = api.get_aeroplanes(country)
    aeroplanes: List[Aeroplane] = [Aeroplane.from_raw(p) for p in raw_data]

    filtered_planes = filter_aeroplanes(aeroplanes, filter_words)
    ranged_planes = get_aeroplanes_by_altitude(filtered_planes, altitude_range)
    sorted_planes = sort_aeroplanes(ranged_planes)
    top_planes = get_top_aeroplanes(sorted_planes, top_n)

    print("\nТоп самолетов:")
    for i, plane in enumerate(top_planes, 1):
        print(f"{i}. {plane}")


if __name__ == "__main__":
    user_interaction()
