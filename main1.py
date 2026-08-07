print("======= Programa de Cifragem e Decifragem =======")
entrada = str(input("1. Cifrar \n 2. Decifrar \n "))
if entrada == "1":
    tipocifra = str(input("Escolha o tipo de cifra: \n A: Cifra de César \n B: Cifra de Vigenère \n C: Cifra de Atbash \n D: Morse \n E: Ascii \n"))
    if tipocifra == "A" or "a":
        cesarmsg = str(input("Informe a mensagem que deseja cifrar:"))
        
    elif tipocifra == "B" or "b":
        cesarmsg = str(input("Informe a mensagem que deseja cifrar:"))

    elif tipocifra == "C" or "c":
        cesarmsg = str(input("Informe a mensagem que deseja cifrar:"))
    elif tipocifra == "D" or "d":
        cesarmsg = str(input("Informe a mensagem que deseja cifrar:"))
    elif tipocifra == "E" or "e":
        cesarmsg = str(input("Informe a mensagem que deseja cifrar:"))
    else:
        print("Esta não é uma entrada válida.")

elif entrada == "2":
  tipocifra = str(input("Escolha o tipo de cifra: \n A: Cifra de César \n B: Cifra de Vigenère \n C: Cifra de Atbash \n D: Morse \n E: Ascii \n"))
  if tipocifra == "A" or "a":
          cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))
          
  elif tipocifra == "B" or "b":
          cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))

  elif tipocifra == "C" or "c":
          cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))
  elif tipocifra == "D" or "d":
          cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))
  elif tipocifra == "E" or "e":
          cesarmsg = str(input("Informe a mensagem que deseja decifrar:"))
  else:
          print("Esta não é uma entrada válida.")

else:
  print("Esta não é uma entrada válida.")
