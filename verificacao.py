import os


def verifica_entradas(entrada):
    valores_validos = [2,8,10,16]
    try:
        entrada = int(entrada)
        if entrada in valores_validos:
            return entrada
        mensagem_erro()
    except:
        mensagem_erro()


def mensagem_erro():
        os.system("clear")
        print("\033[1;91m")
        print("{:^40}".format("Você digitou algo inválido."))
        print("Reinicie o programa e tente novamente.\n")
        quit()

def verifica_numero(numero):
    for caractere in numero:
        if numero == ' ':
            mensagem_erro()        
    return numero