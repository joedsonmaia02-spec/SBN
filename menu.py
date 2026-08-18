from codificacao_morse import codifica_morse
from codificacao_morse import decodifica_morse
from  codificacao_vigenere import codificaVigenere
from codificacao_ascii import codificar_ascii
from codificacao_ascii import decodificar_ascii

while 1:
    entrada = str(input("======= Programa de Cifragem e Decifragem ======= \n  1. Cifrar \n 2. Decifrar \n  3. Sair \n"))
    if entrada=="1":
        tipocifra = str(input("Escolha o tipo de cifra: \n A: Cifra de César \n B: Cifra de Vigenère \n C: Cifra de Atbash \n D: Morse \n E: Ascii \n")).upper()

        if tipocifra == "A":
            cesarmsg = str(input("Informe a mensagem que deseja cifrar:"))


        elif tipocifra == "B":
            codificaVigenere()


        elif tipocifra == "C":
            cesarmsg = str(input("Informe a mensagem que deseja cifrar:"))

        elif tipocifra == "D":
            codifica_morse()

        elif tipocifra == "E":
            texto_de_entrada = str(input("Informe a mensagem que deseja cifrar:"))

        else:
            print("Esta não é uma entrada válida.")
            print("Selecione uma um dos abaixo: ")
            tipocifra = str(input("Escolha o tipo de cifra: \n A: Cifra de César \n B: Cifra de Vigenère \n C: Cifra de Atbash \n D: Morse \n E: Ascii \n")).upper()

    elif entrada == "2":
        tipocifra = str(input("Escolha o tipo de cifra: \n A: Cifra de César \n B: Cifra de Vigenère \n C: Cifra de Atbash \n D: Morse \n E: Ascii \n")).upper()

        if tipocifra == "A":
            cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))

        elif tipocifra == "B":
            cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))

        elif tipocifra == "C":
            cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))

        elif tipocifra == "D":
            decodifica_morse()

        elif tipocifra == "E":
            texto_em_ascii = str(input("Informe a mensagem que deseja decifrar:"))

        else:
            print("Selecione um tipo de cifra válido ")
            str(input("Escolha o tipo de cifra: \n A: Cifra de César \n B: Cifra de Vigenère \n C: Cifra de Atbash \n D: Morse \n E: Ascii \n")).upper()

    elif entrada=="3":
        print("="*20,"\n","Sistema encerrado","\n","="*20)
        break
