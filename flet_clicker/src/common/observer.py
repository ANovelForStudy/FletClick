from abc import ABC, abstractmethod
from typing import Any


class Observer(ABC):
    """
    Интерфейс наблюдателя. Объявляет метод уведомления, который издатели
    используют для оповещения своих подписчиков
    """

    @abstractmethod
    def update(self, value: Any, subject: "Subject") -> None:
        pass


class Subject(ABC):
    """
    Интерфейс издателя. Объявляет набор методов для управления подписчиками
    """

    @abstractmethod
    def add_observer(self, observer: "Observer") -> None:
        """
        Подписывает наблюдателя на изменения издателя
        """
        pass

    @abstractmethod
    def remove_observer(self, observer: "Observer") -> None:
        """
        Лишает наблюдателя подписки на изменения издателя
        """
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        """
        Уведомляет всех подписанных на изменения издателя наблюдателей о событии
        """
        pass
