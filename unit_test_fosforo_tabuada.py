##TESTE UNITÁRIO FÓSFORO

import pytest

def calcular_fosforo(num1, num2):
    return num1 * num2

def unit_calcular_fosforo():
    num1 = 2
    num2 = 40
    resultado_esperado = 80
    # parte 2 executa
    resultado_atual = calcular_fosforo(num1, num2)
    assert resultado_esperado == resultado_atual



# MLEHOR PARA TABUADA
# def tabuada(valor):
#     lista_resultado = []
#     for numero in range(11):
#             resultado = numero * int((valor))
#             print(f'{numero} * {valor} = {resultado}')
#             lista_resultado.insert(numero,resultado)
#     return lista_resultado
#
# #Teste unitário tabuada
# def test_tabuada():
#
#         # 1- Configura / Prepara
#         valor = 3 #input
#         resultado_esperado = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30] #output
#
#         # 2- Executa
#         resultado_atual = tabuada(valor)
#
#         # 3- Check / Valida
#         assert resultado_atual == resultado_esperado



####MELHOR CÓDIGO DE FOSFURO E TESTE UNITÁRIO
    # def calcular_fosforos():
    #     caixa = input("Digite a quantidade de caixa de fósforos: ")
    #     try:
    #         caixa2 = int(caixa)
    #         if caixa2 >= 0:
    #             return 'A quantidade de fósforos é {}'.format(caixa2 * 40)
    #         else:
    #             return 'Valor inválido !'
    #     except ValueError:
    #         return 'Obrigatório caracter numérico!!!'
    #
    # ######## TESTES FÓSFOROS ###############
    # def test_calcular_fosforos_OK():
    #     with mock.patch.object(builtins, 'input', lambda _: 10):
    #         assert calcular_fosforos() == 'A quantidade de fósforos é 400'
    #
    # def test_calcular_fosforos_NOK():
    #     with mock.patch.object(builtins, 'input', lambda _: '-1'):
    #         assert calcular_fosforos() == 'Valor inválido !'
    #
    # def test_calcular_fosforos_NOK2():
    #     with mock.patch.object(builtins, 'input', lambda _: 'teste'):
    #         assert calcular_fosforos() == 'Obrigatório caracter numérico!!!'



    # import pytest
    #
    # def calcular_fosforos(numero):
    #     return numero * 40
    # Teste unitário calcular_fosforos
    # def test_calcular_fosforos():
    #     assert calcular_fosforos(5) == 200
    # def tabuada(valor):
    #     lista_resultado = []
    #     for numero in range(11):
    #         resultado = numero * int((valor))
    #         print(f'{numero} * {valor} = {resultado}')
    #         lista_resultado.insert(numero, resultado)
    #     return lista_resultado
    #
    # # Teste unitário tabuada
    # def test_tabuada():
    #
    #     # 1- Configura / Prepara
    #     valor = 3  # input
    #     resultado_esperado = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]  # output
    #
    #     # 2- Executa
    #     resultado_atual = tabuada(valor)
    #
    #     # 3- Check / Valida
    #     assert resultado_atual == resultado_esperado
    #
    # if name == 'main':
    #     # Imprimir quantidade de palitos de fosforos
    #     quantidade = input(f'Digite a quantidade de caixa de fosforo: ')
    #     resultado = calcular_fosforos(int(quantidade))
    #     print(f'A quantidade de palitos de fosforos é, {resultado}')
    #
    #     # Tabuada - Main
    #     valor_tabuada = input(f'Qual valor você deseja ver a tabulada?: ')
    #     print(f'*** TABUADA DO {valor_tabuada} ***')
    #     tabuada(valor_tabuada)