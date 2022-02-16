from coleta_dados import *

if base_entrada == 10:
    numero_em_decimal = numero

else: #Converte para decimal
    numero_string = str(numero)
    numero_string = numero_string[::-1]
    tamanho_numero = len(numero_string)
    soma = 0
    for index in tamanho_numero:
        algarismo =  int(numero_string[index])
        soma += (base_entrada**index)*algarismo
    numero_decimal = int(soma)

if base_saida == 10:
    numero_final = numero_decimal

elif:
    