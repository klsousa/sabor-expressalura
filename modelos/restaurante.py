from modelos.avaliacao import Avaliacao #Importando o metodo avaliacao

class Restaurante:
    restaurantes = []

    #criando construtor
    #self é a referência atual do objeto que estamos usando (é um nome convencionado)
    def __init__(self, nome, categoria): #esta é uma função reservada "dunder method", já existente em toda classe
        #aqui definimos os atributos (características) da classe (uma entidade)
        self._nome = nome.title()
        self._categoria = categoria.upper()
        #a avaliação será gerada no construtor da classe restaurante. Assim, toda vez que criamos um restaurante, queremos destacar que ele pode ter várias avaliações. Para isso, atribuímos self._avaliacao = [] como uma lista
        self._avaliacao = []
        # _ativo não foi declarado.
        self._ativo = False #com o _ antes de 'ativo', estamos indicando que este é um atributo privado. não queremos que ninguem o altere
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    #Método da classe. e não do objeto
    @classmethod
    def listar_restaurantes(cls):#Convenção usar argumento cls
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}') 
    
    
    @property
    def ativo(self):
        return '☑'if self._ativo else '☐'
    
    #Método de ativar o estado / Método para os Objetos
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:   
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property #Para ler as informações
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        #Vamos passar soma_das_notas e usar um operador do Python chamado sum() para realizar essa soma. Todas as notas estão em Avaliacao e contém ._nota ("ponto", "underline", "nota").
        #Então, de alguma forma, teríamos que acessar essa informação. Portanto, vamos informar que desejamos pegar todas as avaliações e, para cada avaliação, a única informação que queremos é a nota, que deve ser somada: soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao).
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        # funcao len() retorna o comprimento de um objeto
        quantida_de_notas = len(self._avaliacao)
        #As avaliações são: 5; 4.7; 4.8; etc. Bem lembrado! Precisamos, de alguma forma, arredondar e garantir que sempre teremos uma casa decimal. Existe uma função no Python
        # chamada de round() pega as somas e transforma e casa decimal / função round arredondar números para o mais próximo
        media = round(soma_das_notas / quantida_de_notas, 1) # o 1 no final e para colocar quantas casas decimais queremos
        return media





""" class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.duracao = 355

print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')
 """
