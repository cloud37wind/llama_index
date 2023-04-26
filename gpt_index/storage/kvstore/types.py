from abc import ABC, abstractmethod
from typing import Dict, Optional

DEFAULT_COLLECTION = "data"


class BaseKVStore(ABC):
    @abstractmethod
    def put(self, key: str, val: dict, collection: str = DEFAULT_COLLECTION) -> None:
        pass

    @abstractmethod
    def get(self, key: str, collection: str = DEFAULT_COLLECTION) -> Optional[dict]:
        pass

    @abstractmethod
    def get_all(self, collection: str = DEFAULT_COLLECTION) -> Dict[str, dict]:
        pass

    @abstractmethod
    def delete(self, key: str, collection: str = DEFAULT_COLLECTION) -> None:
        pass


class BaseInMemoryKVStore(BaseKVStore):
    @abstractmethod
    def persist(self) -> None:
        pass

    @abstractmethod
    def load(self) -> None:
        pass