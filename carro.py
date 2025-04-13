from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas, cor):
        super().__init__(marca, modelo)
        self.portas = portas
        self.cor = cor 

    def __str__(self):
        return f"{super().__str__()} - {self.portas} portas"

    def ligar(self):
        if not self._ligado:
            self._ligado = True
            print(f"{self.marca} {self.modelo} ligado.")
        else:
            print(f"{self.marca} {self.modelo} já está ligado.")
    