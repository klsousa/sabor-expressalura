from veiculo import Veiculo

# 5- Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.
class Moto(Veiculo):
    def __init__(self, marca, modelo,tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        status = "Ligado" if self._ligado else "Desligado"
        return f"{self.marca} {self.modelo} - Tipo: {self.tipo} - Status: {status}"