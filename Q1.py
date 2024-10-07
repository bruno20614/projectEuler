#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below the provided parameter value number.

def soma_divisiveis_por_3_e_5(number):
    soma=0

    for i in range (3,number):
            if i % 3 == 0 or i % 5 == 0:
                soma += i


    return soma

resultado = soma_divisiveis_por_3_e_5(10)
print(resultado)