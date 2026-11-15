from abc import ABC, abstractmethod


class IPatronRule(ABC):
    @abstractmethod
    def matches(self, data: list) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError


class IObserver(ABC):
    @abstractmethod
    def update(self, alerta: str) -> None:
        raise NotImplementedError


class IAlertaRepository(ABC):
    @abstractmethod
    def save(self, alerta: str) -> None:
        raise NotImplementedError
