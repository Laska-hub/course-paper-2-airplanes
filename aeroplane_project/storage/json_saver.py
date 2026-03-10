import json
from typing import Any, Dict, List

from aeroplane_project.models.aeroplane import Aeroplane
from aeroplane_project.storage.file_adapter import AbstractFileSaver


class JSONSaver(AbstractFileSaver):
    def __init__(self, filename: str = "aeroplanes.json") -> None:
        self._filename: str = filename

    def add_aeroplane(self, aeroplane: Aeroplane) -> None:
        data = self._load_file()
        if aeroplane.callsign not in [a["callsign"] for a in data]:
            data.append(aeroplane.__dict__)
            self._save_file(data)

    def get_aeroplanes(self, **criteria: Any) -> List[Dict[str, Any]]:
        data = self._load_file()
        return [a for a in data if all(a[k] == v for k, v in criteria.items())]

    def delete_aeroplane(self, aeroplane: Aeroplane) -> None:
        data = self._load_file()
        data = [a for a in data if a["callsign"] != aeroplane.callsign]
        self._save_file(data)

    def _load_file(self) -> List[Dict[str, Any]]:
        try:
            with open(self._filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def _save_file(self, data: List[Dict[str, Any]]) -> None:
        with open(self._filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
