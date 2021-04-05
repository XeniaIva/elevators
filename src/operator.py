"""
Из доки: IOperator описывает функционал диспетчера
вопрос нейминга не разрешён
"""
from src.elevator import Elevator


class Operator:
    def __init__(self, elevator: Elevator):
        """
        Из доки:
        Содержит ссылку на экземпляр лифта
        Зачем?
        Разве диспетчер не следит за несколькими лифтами?
        Кажется, нужно несколько лифтов
        """
        self.elevator = elevator
    
    def open_doors(self):
        self.elevator.open_doors()
    
    def close_doors(self):
        self.elevator.close_doors()

    def light_on(self):
        self.elevator.turn_light_on()
    
    def light_off(self):
        self.elevator.turn_light_off()
    
    def call(self):
        """
        В доке написан про попытку
        ToDo: Реализовать именно попытку
        """
        try:
            self.elevator.call_dispatcher()
        except Exception as e:
            pass
    
    def move_to_floor(self, floor: int):
        self.elevator.move_to_floor(floor)
    
    def get_elevator_state(self):
        """
        Состояние кабины лифта
        Какое состояние???
        мб в классе лифта собрать инфу со всех датчиков
        """
        return {}

    def restart(self):
        """
        ToDo: реализовать перезагрузку кабины
        """
        pass