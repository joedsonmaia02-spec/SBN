morse = {'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..','0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-',   ',': '--..--',   '?': '..--..',   "'": '.----.',
    '!': '-.-.--',   '/': '-..-.',    '(': '-.--.',    ')': '-.--.-',
    '&': '.-...',    ':': '---...',   ';': '-.-.-.',   '=': '-...-',
    '+': '.-.-.',    '-': '-....-',   '_': '..--.-',   '"': '.-..-.',
    '$': '...-..-',  '@': '.--.-.','Ã': '.--.-',    'Á': '.--.-',    'À': '.--.-',    'Â': '.--.-',
    'É': '..-..',    'Ê': '..-..',    'Í': '..',       'Ó': '---.',
    'Õ': '---.',     'Ú': '..--',     'Ç': '-.-..',}

def codificar_morse():  # Codificação de Texto para Morse
    while True:
        texto = input('Digite uma palavra (ou "SAIR" para encerrar): ').upper()

        if texto == "SAIR":
            print("Encerrando...")
            break

        codigo = ""
        for letra in texto:
            if letra == " ":
                codigo += "/ " 
                continue

            try:
                codigo += morse[letra] + " "
            except KeyError:
                print(f'Aviso: "{letra}" não é uma letra ou número válido e foi ignorado.')

        return(codigo)

morse_invertido = {valor: chave for chave, valor in morse.items()}


def decodificar_morse():
    while True:
        codigo = input('Digite o código morse (use "/" entre palavras, ou "/SAIR" para encerrar): ')

        if codigo.strip().upper() == "/SAIR":
            print("Encerrando...")
            break

        palavras = codigo.strip().split("/")
        texto_final = []

        for palavra in palavras:
            simbolos = palavra.split()
            texto = ""
            for simbolo in simbolos:
                try:
                    texto += morse_invertido[simbolo]
                except KeyError:
                    print(f'Aviso: "{simbolo}" não é um código morse válido e foi ignorado.')

            texto_final.append(texto)

        return(" ".join(texto_final))
        
