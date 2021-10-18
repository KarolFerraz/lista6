####LISTA 6 - KAROLYNE FERRAZ ####

def print_hi(name):
    print(f'Olá cliente {name}, vamos calcular a quantidade de fósforo na caixa para você!')

#EXERCICIO 1 fosforo
def calcular_fosforo(qnt):
    return qnt * 40

#EXERCICIO 2 tabuada
def tabuada(numero):
    for contagem in range(1,11):
        print(f'{numero} x {contagem} = {numero*contagem}')



####################

if __name__ == '__main__':
    print_hi('Dona Ana')

#EXERCICIO 1
    #calcular palito
    qnt = input(f'Digite a quantidade de caixa de fósforo: ')
    resultado = calcular_fosforo(int(qnt))
    print(f'A quantidade de fósforo na(s) caixa(s) é de {resultado} palito(s)')

#EXERCICIO 2
    #calcular tabuada
    numero = int(input('Digite o número para ver sua tabuada até 10: '))
    print(f'A tabuada do número {numero} é:')
    tabuada(numero)
