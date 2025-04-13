from abc import abstractmethod


class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self._ligado}"

    @abstractmethod
    def ligar(self):
        pass

