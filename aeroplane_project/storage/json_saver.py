import json
from pathlib import Path
from typing import Any


class JSONSaver:
    """
    Класс для сохранения и загрузки данных в формате JSON
    """

    def __init__(self, path: str):
        self.path = Path(path)

    def save(self, data: Any) -> None:
        """
        Сохраняет данные в JSON файл
        """
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load(self) -> Any:
        """
        Загружает данные из JSON файла, если файл существует
        """
        if not self.path.exists():
            return None
        with self.path.open("r", encoding="utf-8") as f:
            return json.load(f)
