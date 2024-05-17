#Criar um dicionario
informacoes_pessoa = {'nome':'Kelvin','idade': 23,'cidade':'Nova iguaçu'}
#Atualização de idade
informacoes_pessoa['idade'] = 25
#Adicionando Profissão
informacoes_pessoa['Profissao'] = 'Engenheiro'
#Remoção de Elemento
del informacoes_pessoa['cidade']
#3 - Uma possível abordagem para criar um dicionário que apresente os números de 1 a 5 e seus respectivos quadrados é a seguinte:
numero_quadrados = {x: x**2 for x in range(1,6)}
print(numero_quadrados)
#4 - Para verificar a existência de uma chave no dicionário, você pode utilizar a seguinte estrutura:
pessoa = {'nome':'Vanessa','idade': 23,'cidade':'Nova iguaçu'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionario.")
else:
    print("A chave 'nome' não existe no dicionario.")
#5 - Para contar a frequência de cada palavra em uma frase, você pode utilizar o seguinte código:
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra]
