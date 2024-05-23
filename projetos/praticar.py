lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try: 

    for numero in lista_numeros:
        soma += numero
        print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
""" Exception é uma classe base para todas as exceções em Python. 
    Capturar Exception permite lidar com qualquer tipo de exceção que possa ocorrer no bloco try. 
    O as e é opcional, mas é frequentemente usado para acessar informações detalhadas sobre a exceção, como mensagens de erro.
 """
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try: 
    for valor in lista_valores:
        soma_valores += valor
        media = soma_valores / len(lista_valores)
        print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}") 
""" 
    ZeroDivisionError é uma exceção específica que ocorre quando há uma tentativa de divisão por zero. 
    Este bloco except é destinado a lidar especificamente com esse tipo de erro.
 """





""" lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_de_nome = ['kelvin', 'vanessa','manoel']
lista_de_anos = [2000,2001,1970]
 """
""" Lista numeros """
""" for numero in lista_de_numeros:
    print(numero) """

""" soma numeros """
""" soma_numeros = 0

for i in range(1,11,2):
    soma_numeros += i
    print(soma_numeros) """

""" números de 1 a 10 de forma decrescente """
""" for i in range(10,0,-1):
    print(i) """

""" tabuada interativa """
""" numero_tabuada = int(input("Digite um numero para a tabuada: "))

for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}") """