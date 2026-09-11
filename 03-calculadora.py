def somar():
        n1 = float(input('digite um número: '))
        n2 = float(input('digite outro número: '))
        resultado = n1 + n2
        print(resultado)
def subtrair():
        n1 = float(input('digite um número: '))
        n2 = float(input('digite outro número: '))
        resultado = n1 - n2
        print(resultado)
def multiplicar():
        n1 = float(input('digite um número: '))
        n2 = float(input('digite outro número: '))
        resultado = n1 * n2
        print(resultado)
def dividir():
        n1 = float(input('digite um número: '))
        n2 = float(input('digite outro número: '))
        resultado = n1 / n2
        print(resultado)

while True:
    print('Calculadora')
    print('1. SOMA')
    print('2. SUBTRAÇÃO')
    print('3. MULTIPLICAÇÃO')
    print('4. DIVISÃO')
    print('0. SAIR')

    opcao = input('escolha uma opção: ')
    
    if opcao == '1':
        print('Somando...')
    elif opcao == '2':
        print('Subtraindo...')
    elif opcao == '3':
        print('Multiplicando...')
    elif opcao == '4':
        print('Dividindo...')
        
    elif opcao == '0':
        print('Saindo do sistema...')
        break

    
    else:
        print('opção inválida, tente novamente!')
    break

