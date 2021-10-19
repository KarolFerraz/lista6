####LISTA 6 - KAROLYNE FERRAZ ####
#import
import pytest

def print_hi(name):
    print(f'Olá cliente {name}, vamos calcular a quantidade de fósforo na caixa para você!')

#EXERCICIO 1 fosforo
def calcular_fosforo(qnt):
    return qnt * 40

#EXERCICIO 2 tabuada
def tabuada(numero):
    for contagem in range(1,11):
        print(f'{numero} x {contagem} = {numero*contagem}')


#EXERCICIO 2 tabuada MELHORADA
def tabuada_better(numero):
    resposta_STR = ''
    for contagem in range(1,11):
        resultado = numero * contagem
        print(f'{numero} x {contagem} = {resultado}')
        if resposta_STR == 1:
            resposta_STR = str(resultado)
        else:
            resposta_STR = resposta_STR + ',' + str(resultado)
        #print(resposta_STR)
    return resposta_STR


def tabuada_FOR_IF(num):
    resposta = ''
    for i in range(1,11):               # i é abreviação de iterator / incremento
        resultado = i * num
        print(f'\n {i} x {num} = {resultado}') # 2
        if i == 1:
            resposta = str(resultado)
        else:
            resposta = resposta + ',' + str(resultado)

    return resposta

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


##testeunitárioERRADO
def test_tabuada():
    numero = 2
    resposta_esperada = ',2,4,6,8,10,12,14,16,18,20'
    assert tabuada_better(numero) == resposta_esperada
    print(f'\n Tabuada do {numero} \n {resposta_esperada}')


def test_tabuada_FOR_IF():
    num = 4
    resposta_esperada = '2,4,6,8,10,12,14,16,18,20'
    assert tabuada_FOR_IF(num) == resposta_esperada
    print(f'\n Tabuada do {num} \n {resposta_esperada}')

