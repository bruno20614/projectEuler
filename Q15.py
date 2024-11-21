#Escreva uma função recursiva em python que receba um inteiro K.Essa função deve retornar a soma dos digitos impares.Exemplo de entrada
from Q1 import resultado


def RetornarSomaDigitosImpares(number):

    if number == 0:
        return 0

    ultimo_digito = number % 10

    if ultimo_digito % 2 != 0:
        return ultimo_digito + RetornarSomaDigitosImpares(number // 10)
    else:
        return RetornarSomaDigitosImpares(number // 10)

numero = int(input("Digite um número: "))

resultado = RetornarSomaDigitosImpares(numero)
print(f"A soma dos dígitos ímpares é: {resultado}")