from abc import ABC, abstractmethod

from requests import Response


class APIClient(ABC):
    @abstractmethod
    def get(self, endpoint: str, params: dict | None = None, headers: dict | None = None) -> Response:
        pass
