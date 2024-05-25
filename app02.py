from modelos.restaurante import Restaurante # From e usado para buscar o local aonde esta localizado a sua aplicação.
from cardapio.bebida import Bebida
from cardapio.prato import Prato

restaurante_praca = Restaurante('praca', 'Gourmet')
bebida_suco = Bebida('Suco Laranja',5.0,'grande')
prato_paozinho = Prato('Paozinho',2.00,'O melhor pão da cidade')



def main():
    print(bebida_suco)
    print(prato_paozinho)


if __name__ == '__main__':
    main()

#  O __pycache__ é uma forma mais simples do Python interpretar aquele módulo que estamos importando. Ou seja, é um diretório que o Python cria para armazenar os arquivos compilados em bytecode. Que é uma forma que ele tem de interpretar aqueles códigos de uma maneira muito mais simples do que no arquivo original.
#   É uma espécie de arquivo que otimiza o desempenho do aplicativo. No entanto, destina-se ao interpretador do Python que gerou o arquivo, para que o computador o compreenda, e não necessariamente para nós, correto? Legal.
    

"""1. Documentação oficial do Python (gratuito, português, texto)
Fonte oficial de informações sobre a linguagem Python. Aqui você encontra informações sobre os conceitos relacionados ao desenvolvimento da linguagem, tutoriais, referências, informações de atualizações, boas práticas e exemplos.

2. Artigo sobre classes com Python (gratuito, português, texto)

Mais sobre a Programação Orientada a Objetos através de exemplos de código em Python explorando as características desse conceito.

3. W3S de Python (gratuito, inglês, texto)

Recurso educacional online que fornece tutoriais, referências e exemplos práticos para aprender Python, uma linguagem de programação de alto nível.

4. Documentação oficial do Python sobre Classes (gratuito, inglês, texto)

Documentação oficial do Python 3, especificamente para a seção do tutorial que aborda o conceito de classes em Python. A documentação oficial do Python é mantida pela Python Software Foundation e é uma fonte autoritativa de informações sobre a linguagem de programação Python. """