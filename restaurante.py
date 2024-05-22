class Restaurante:
    restaurantes = []

    #criando construtor
    #self é a referência atual do objeto que estamos usando (é um nome convencionado)
    def __init__(self, nome, categoria): #esta é uma função reservada "dunder method", já existente em toda classe
        #aqui definimos os atributos (características) da classe (uma entidade)
        self._nome = nome.title()
        self._categoria = categoria.upper()
        # _ativo não foi declarado.
        self._ativo = False #com o _ antes de 'ativo', estamos indicando que este é um atributo privado. não queremos que ninguem o altere
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    #Método da classe. e não do objeto
    @classmethod
    def listar_restaurantes(cls):#Convenção usar argumento cls
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}') 
    
    
    @property
    def ativo(self):
        return '☑'if self._ativo else '☐'
    
    #Método de ativar o estado / Método para os Objetos
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()





""" class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.duracao = 355

print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')
 """
