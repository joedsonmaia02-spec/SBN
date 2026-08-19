from codificacao_cesar import codificar_cesar, decodificar_cesar
from codificacao_vigenere import codificar_vigenere, decodificar_vigenere
from codificacao_atbash import codificar_atbash, decodifica_Atbash
from codificacao_morse import codificar_morse, decodificar_morse
from codificacao_ascii import codificar_ascii, decodificar_ascii
from file_and_list_functions import salva_em_arquivo,criar_lista_entrada,open_file_read,receber_path
from break_cipher import quebrar_cifra

print("======= Programa de Cifragem e Decifragem =======")

entrada = str(input("1. Cifrar \n2. Decifrar\n3. Quebrar cifra Cesar\nOpção:"))

if entrada == "1":
    tipocifra = input("Escolha o tipo de cifra: \n A: Cifra de César \n B: Cifra de Vigenère \n C: Cifra de Atbash \n D: Morse \n E: Ascii \nOpção:")
    if tipocifra == "A":
        cesarmsg = str(input("Informe a mensagem que deseja cifrar:"))
        key = int(input("Informe chave que deseja usar(1-26):"))
        msg_codificada = codificar_cesar(cesarmsg, key)
        print(msg_codificada)
    elif tipocifra == "B":
        msg_codificada = codificar_vigenere()
        print(msg_codificada)
    elif tipocifra == "C":
        msg_codificada = codificar_atbash()
        print(msg_codificada)
    elif tipocifra == "D":
        msg_codificada=codificar_morse()
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
        cesarmsg = input("Informe a mensagem que deseja decifrar:")
        key = int(input("Informe chave que deseja usar(1-26):"))
        msg_decodificada = decodificar_cesar(cesarmsg, key)
        print(msg_decodificada)
    elif tipocifra == "B":
        msg_decodificada = str(input("Informe a mensagem que deseja decifrar:"))
    elif tipocifra == "C":
        msg_decodificada = decodifica_Atbash()
        print(msg_decodificada)
    elif tipocifra == "D":
        msg_decodificada=decodificar_morse()
        print(msg_decodificada)
    elif tipocifra == "E":
        ascii_msg = input("Informe a mensagem que deseja decifrar:")
        msg_decodificada = decodificar_ascii(ascii_msg)
        print(msg_decodificada)
    else:
        print("Esta não é uma entrada válida.")
    
    write_on_file_condition=input("Deseja gravar o texto decodificado em um arquivo de texto?(S/N): ")
    if write_on_file_condition=="S":
        salva_em_arquivo(msg_decodificada)
elif entrada == "3":
    break_condition=input("Deseja quebrar a cifra de cesar de um Arquivo ou Texto?(A/T): ")
    if break_condition=="A":
        chave=quebrar_cifra(open_file_read(receber_path()))
        print("A chave é:",chave)
    if break_condition=="T":
        chave=quebrar_cifra(criar_lista_entrada(input("Insira a frase: ")))
        print("A chave é:",chave)
else:
    print("Esta não é uma entrada válida.")
