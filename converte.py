from coleta_dados import *

dicionario_conversor = {2:bin,8:oct,16:hex}

if base_entrada == 10:
    numero_em_decimal = numero

else: #Converte para decimal
    numero_em_decimal = int(numero,base=base_entrada)

if base_saida == 10:
    numero_final = numero_em_decimal

else:
    numero_final = dicionario_conversor[base_saida](numero_em_decimal)
    numero_final = numero_final[2::]