from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, name) -> None:
        self.name = name
        self._money = 100
        self.__paisa = 1000
        pass

    @abstractmethod
    def start(self, number=None) -> str:
        return "Car Started Main"
    
    def get_paisa(self):
        return self.__paisa


class CarA(Car):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def start(self, number=None) -> str:
        print(self._money)
        return "CarA started "

    

c1 = CarA(name='Testing')
print(c1.start())
print(c1.get_paisa())
