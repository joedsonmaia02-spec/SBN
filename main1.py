from codificacao_cesar import codificar_cesar
from codificacao_vigenere import codificaVigenere
from codificacao_atbash import codificaAtbash
from codificacao_morse import codifica_morse
from codificacao_ascii import codificar_ascii, decodificar_ascii
print("======= Programa de Cifragem e Decifragem =======")

entrada = str(input("1. Cifrar \n2. Decifrar\nOpção:"))

if entrada == "1":
    tipocifra = input("Escolha o tipo de cifra: \n A: Cifra de César \n B: Cifra de Vigenère \n C: Cifra de Atbash \n D: Morse \n E: Ascii \nOpção:")
    if tipocifra == "A":
        cesarmsg = str(input("Informe a mensagem que deseja cifrar:"))
        key = int(input("Informe chave que deseja usar(1-26):"))
        msg_codificada = codificar_cesar(cesarmsg, key)
        print(msg_codificada)
    elif tipocifra == "B":
        msg_codificada = codificaVigenere()
        print(msg_codificada)
    elif tipocifra == "C":
        msg_codificada = codificaAtbash()
        print(msg_codificada)
    elif tipocifra == "D":
        codifica_morse()
    elif tipocifra == "E":
        ascii_msg = input("Informe a mensagem que deseja cifrar:")
        msg_codificada = codificar_ascii(ascii_msg)
        print(msg_codificada)
    else:
        print("Esta não é uma entrada válida.")

elif entrada == "2":
    tipocifra = str(input(
        "Escolha o tipo de cifra: \n A: Cifra de César \n B: Cifra de Vigenère \n C: Cifra de Atbash \n D: Morse \n E: Ascii \n"))
    if tipocifra == "A":
        cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))
    elif tipocifra == "B":
        cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))
    elif tipocifra == "C":
        cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))
    elif tipocifra == "D":
        cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))
    elif tipocifra == "E":
        cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))
    else:
        print("Esta não é uma entrada válida.")

else:
    print("Esta não é uma entrada válida.")
