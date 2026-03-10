from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

import requests


class AbstractAPI(ABC):
    @abstractmethod
    def _connect(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """Подключение к API"""
        pass

    @abstractmethod
    def get_aeroplanes(self, country: str) -> List[List[Any]]:
        """Получение самолетов по стране"""
        pass


class AeroplanesAPI(AbstractAPI):
    def __init__(self) -> None:
        self.nominatim_url: str = "https://nominatim.openstreetmap.org/search"
        self.opensky_url: str = "https://opensky-network.org/api/states/all?"

    def _connect(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        response = requests.get(url, params=params, headers=headers)
        if response.status_code != 200:
            raise ConnectionError(f"Ошибка запроса: {response.status_code}")
        return response.json()

    def get_aeroplanes(self, country: str) -> List[List[Any]]:
        headers = {"User-Agent": "test-app/1.0"}
        country_clean = country.strip().encode("utf-8", "ignore").decode("utf-8")
        params = {"country": country_clean, "format": "json", "limit": 1}

        data = self._connect(self.nominatim_url, params=params, headers=headers)
        if not data:
            return []

        bbox = data[0]["boundingbox"]
        params_opensky = {
            "lamin": bbox[0],
            "lamax": bbox[1],
            "lomin": bbox[2],
            "lomax": bbox[3],
        }

        aeroplanes_data = self._connect(self.opensky_url, params=params_opensky)
        return aeroplanes_data.get("states", [])
