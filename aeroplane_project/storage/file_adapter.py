from abc import ABC, abstractmethod
from typing import Any, Dict, List


class AbstractFileSaver(ABC):
    @abstractmethod
    def add_aeroplane(self, aeroplane: Any) -> None:
        """Добавить самолет в хранилище"""
        ...

    @abstractmethod
    def get_aeroplanes(self, **criteria: Any) -> List[Dict[str, Any]]:
        """Получить самолеты по критериям"""
        ...

    @abstractmethod
    def delete_aeroplane(self, aeroplane: Any) -> None:
        """Удалить самолет из хранилища"""
