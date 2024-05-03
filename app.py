import os
def exibir_nome_do_programa(): 
    print("""""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

""" def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

def finalizar_app():
    os.system('cls')
    print('Finalizando o app\n')  

def escolher_opcao():

    opcao_escolhida =  int (input('Escolha uma opção: '))
    #opcao_escolhida = int(opcao_escolhida)

    
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurante')
    elif opcao_escolhida == 3:
        print('3. Ativar restaurante')
    else:
        finalizar_app()

if __name__ == '__main__':
    main()
 """








def configurar_tempo_foco():
    tempo = int(input("Digite o tempo de foco (25-45 min): "))
    if tempo < 25:
        print("Valor muito baixo. Configure um tempo maior ou igual a 25 minutos.")
    elif tempo > 45:
        print("Valor muito alto. Configure um tempo menor ou igual a 45 minutos.")
    else:
        print("Tempo configurado para", tempo, "minutos.")



""" #APRENDIZADO

#Verificar o que esta retornando
print(type(opcao_escolhida))
print(type(1))

print('Python na Escola de Programação da Alura')
nome = 'Kelvin'
idade = 23
print(f'Meu nome e {nome} e tenho {idade} anos')
print('A','L','U','R','A',sep='\n')

pi = 3.14159
print(f'O valor arredondado de pi é: {pi}')


pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))

# Criação das Variáveis
nome = 'Lais'
idade = 24

# Abordagem mais simples
print('Meu nome é',nome,'e tenho',idade,'anos.')

# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos.')

# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

# Abordagem da % (Formatação de String Antiga - Python 2)
print('Meu nome é %s e tenho %i anos.'%(nome,idade)) """

