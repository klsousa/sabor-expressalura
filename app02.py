from modelos.restaurante import Restaurante # From e usado para buscar o local aonde esta localizado a sua aplicação.

restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Kelvin', 10)
restaurante_praca.receber_avaliacao('Vanessa', 8)
restaurante_praca.receber_avaliacao('Gui', 3)



def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()

#  O __pycache__ é uma forma mais simples do Python interpretar aquele módulo que estamos importando. Ou seja, é um diretório que o Python cria para armazenar os arquivos compilados em bytecode. Que é uma forma que ele tem de interpretar aqueles códigos de uma maneira muito mais simples do que no arquivo original.
#   É uma espécie de arquivo que otimiza o desempenho do aplicativo. No entanto, destina-se ao interpretador do Python que gerou o arquivo, para que o computador o compreenda, e não necessariamente para nós, correto? Legal.
    