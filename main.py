from carro import Carro
from moto import Moto

def __main__():
    # Criando instâncias de Carro e Moto
    carro1 = Carro("Toyota", "Corolla", 4)
    carro2 = Carro("Ford", "Fiesta", 5)
    moto1 = Moto("Honda", "CB500", 500)

    # Exibindo informações dos veículos
    print(carro1)
    print(moto1)

    # Ligando o carro
    carro1.ligar()

if __name__ == "__main__":
    __main__()