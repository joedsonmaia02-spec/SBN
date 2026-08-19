from codificacao_cesar import codificar_cesar, decodificar_cesar
from codificacao_vigenere import codificaVigenere
from codificacao_atbash import codificaAtbash
from codificacao_morse import codifica_morse
from codificacao_ascii import codificar_ascii, decodificar_ascii
from file_and_list_functions import salva_em_arquivo
print("======= Programa de Cifragem e Decifragem =======")

entrada = str(input("1. Cifrar \n2. Decifrar\nOpção:"))

if entrada == "1":
    tipocifra = input("Escolha o tipo de cifra: \n A: Cifra de César \n B: Cifra de Vigenère \n C: Cifra de Atbash \n D: Morse \n E: Ascii \nOpção:")
    if tipocifra == "A":
        texto = input("Digite o texto codificado: ")
        deslocamento = int(input("Digite o deslocamento usado na codificação: "))
        resultado=codificar_cesar(texto, deslocamento)
        print(resultado)
    elif tipocifra == "B":
        msg_codificada = codificaVigenere()
        print(msg_codificada)
    elif tipocifra == "C":
        msg_codificada = codificaAtbash()
        print(msg_codificada)
    elif tipocifra == "D":
        msg_codificada=codifica_morse()
        print(msg_codificada)
    elif tipocifra == "E":
        ascii_msg = input("Informe a mensagem que deseja cifrar:")
        msg_codificada = codificar_ascii(ascii_msg)
        print(msg_codificada)
    else:
        print("Esta não é uma entrada válida.")
    write_on_file_condition=input("Deseja gravar o texto codificado em um arquivo de texto?(S/N): ")
    if write_on_file_condition=="S":
        salva_em_arquivo(msg_codificada)


elif entrada == "2":
    tipocifra = str(input(
        "Escolha o tipo de cifra: \n A: Cifra de César \n B: Cifra de Vigenère \n C: Cifra de Atbash \n D: Morse \n E: Ascii \n"))
    if tipocifra == "A":
        cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))
    elif tipocifra == "B":
        msg_codificada = str(input("Informe a mensagem que deseja decifrar:"))
    elif tipocifra == "C":
        cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))
    elif tipocifra == "D":
        cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))
    elif tipocifra == "E":
        cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))
    else:
        print("Esta não é uma entrada válida.")
    
    write_on_file_condition=input("Deseja gravar o texto decodificado em um arquivo de texto?(S/N): ")
    if write_on_file_condition=="S":
        salva_em_arquivo(msg_decodificada)

else:
    print("Esta não é uma entrada válida.")
