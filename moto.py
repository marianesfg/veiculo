from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{super().__str__()}, Cilindrada: {self.cilindrada}cc"