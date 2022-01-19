import os 
class Conversor_de_bases:
    
    def __init__(self):
        self.bases = list()
        self.dicionario_numeros = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
        for i in range(10):
            self.dicionario_numeros[str(i)] = i

    # primeira parte do menu
    def primeira_parte(self):
        print("\033[1;36m"+"Seja bem vindo!\n","\033[1;97m")
        print("Serei seu conversor de bases númericas!\n")
        print("Para começar, vamos selecionar qual a base que eu número pertence")
        self.menu()

    # imprime o menu
    def menu(self):
        print("Digite a opção para selecionar:")
        print("2- Binário")
        print("8- Octal")
        print("10- Decimal")
        print("16- Hexadecimal")
        self.bases.append(int(input("Selecione:")))
        if self.valida_entrada():
            self.mensagem_erro()  

    # segunda parte do menu
    def segunda_parte(self):
        print("Agora que você selecionou a primeira opção\n")
        print("Você precisa selecionar a segunda opção")
        self.menu()

    # verifica se a entrada dada e valida 
    def valida_entrada(self):
        self.valores_validos = [2,8,10,16]
        try:
            if not (self.bases[-1] in self.valores_validos):
                return True
            return False
        except:
            return False

    # retorna uma mensagem de erro
    def mensagem_erro(self):
        os.system("clear")
        print("\033[1;91m"+"Você digitou uma opção inválida."+"\033[1;97m")
        print("Reinicie o programa e tente novamente.")
        quit()

    # recebe o valor que será convertido
    def recebe_numero(self):
        self.numero = input("\nAgora é preciso digitar o número que será convertido:")

    # converte de decimal para a ultima base
    def de_decimal(self):
        if self.bases[-1] == 10:
            self.numero_convertido = self.numero_decimal
        else:
            self.numero_convertendo = self.numero_decimal
            self.restos = list()
            while self.numero_convertendo>=self.bases[-1]:
                self.restos.append(self.numero_convertendo % self.bases[-1])
                self.numero_convertendo -= self.numero_convertendo//self.bases[-1]
            print(self.restos)
   
   
   # roda o programa
    def run(self):
        self.primeira_parte()
        self.segunda_parte()
        self.recebe_numero()
        self.para_decimal()
        self.de_decimal()


    # converte para decimal
    def para_decimal(self):
        self.tamanho_numero = len(str(self.bases[0]))
        self.decimal = [self.dicionario_numeros[x] for x in str(self.numero)]
        self.numero_decimal = 0
        for i in range(self.tamanho_numero):
            self.numero_decimal += int(self.decimal[-1*(i+1)])*(self.bases[0]**i)
        print(f'Em decimal{self.numero_decimal}')


roda = Conversor_de_bases()
roda.run()
