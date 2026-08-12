morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
         '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
         '8': '---..', '9': '----.'}

def codifica_morse(): # Codificação de Texto para Morse
    while True:
        texto = input('Digite uma palavra (ou "sair" para encerrar): ').upper()

        if texto == "SAIR":
         break

        codigo = ""
        for letra in texto:
            codigo = codigo + morse.get(letra, "") + " "

        print(codigo)
