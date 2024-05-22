class Pessoa:

    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}'
        else:
            return f'Ola, sou {self.nome}'
    def aniversario(self):
        self.idade += 1

pessoa1 = Pessoa(nome='Kelvin', idade=23, profissao='Programador')




# Imprimindo informações iniciais
print("Informações Iniciais")
print(pessoa1)

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.aniversario()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(pessoa1)

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao)