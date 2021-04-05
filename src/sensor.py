from abc import ABC, abstractmethod


class AbstractSensor(ABC):
    @abstractmethod
    def get_current_state(self, *args, **kwargs):
        """
        Снятие показаний с датчика
        Какие входные параметры???
        """
        pass

    @abstractmethod
    def trigger(self):
        """
        Оповещение оператора об изменении параметра
        """
        pass


class DoorSensor(AbstractSensor):
    """
    Датчик помехи дверей
    """
    def __init__(self):
        """
        Подумать какие параметры нужны
        """
        pass

    def get_current_state(self, *args, **kwargs):
        pass

    def trigger(self):
        pass
