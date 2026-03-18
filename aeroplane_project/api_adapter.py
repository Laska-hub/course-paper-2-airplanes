from typing import List

import requests


def get_raw_data(url: str) -> List[List]:
    """Получает данные с API OpenSky."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("states", [])
    except Exception as exc:
        raise RuntimeError(f"Ошибка API: {exc}") from exc
