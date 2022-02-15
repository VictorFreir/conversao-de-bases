import os
import verificacao

ciano = "033[\1;36m"
branco = "\033[1;97m"
titulo = "Seja bem vindo!"

print("{:^40}".format(titulo))
print("Serei seu conversor de bases númericas!")
print("Para começar, vamos selecionar a base inicial e a base desejada do seu número:")
print("2- Binário")
print("8- Octal")
print("10- Decimal")
print("16- Hexadecimal")
base_entrada = input("Selecione:")
print("Agora a base final")
base_saida = input("Selecione:")

base_entrada = verificacao.verifica_entradas(base_entrada)
base_saida = verificacao.verifica_entradas(base_saida)

os.system('clear')
print('Entradas válidas!')
print('Agora digite o número a ser convertido') 
print(f'OBS: caso o número que você digitou tenha algarismos que não existem na base,' 
        ' será retornado um número errado e não um erro.')
numero = input()
numero = verificacao.verifica_numero(numero)
os.system('clear')