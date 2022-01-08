import os 
class Conversor_de_bases:
    def __init__(self):
        return
    def menu(self):
        print("\033[1;36m"+"Seja bem vindo!\n","\033[1;97m")
        print("Serei seu conversor de bases númericas!\n")
        print("Para começar, vamos selecionar qual a base que eu número pertence")
        print("Digite a opção para selecionar:")
        print("1- Binário")
        print("8- Octal")
        print("10- Decimal")
        print("16- Hexadecimal")
        self.base_primaria = input("Selecione:")
        if not self.valida_entrada(self.base_primaria):
            self.mensagem_erro()
        return

    def valida_entrada(self,entrada):
        self.valores_validos = [2,8,10,16]
        self.entrada = entrada
        if self.entrada in self.valores_validos:
            return True
        return False

    def mensagem_erro(self):
        if os.name == "nt":
            os.system("clear")
        else:
            os.system("cls")
        print("\033[1;91m"+"Você digitou uma opção inválida."+"\033[1;97m")
        print("Reinicie o programa e tente novamente.")


roda = Conversor_de_bases()
roda.menu()
