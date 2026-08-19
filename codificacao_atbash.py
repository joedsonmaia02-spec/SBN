atbash = {'A':'Z','B':'Y','C':'X','D':'W','E':'V','F': 'U', 
          'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 
          'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 
          'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G', 'U': 'F', 
          'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A', 
          'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 
          'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 
          'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 
          'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 
          'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 
          'z': 'a', '0': '9', '1': '8', '2': '7', '3': '6', 
          '4': '5', '5': '4', '6': '3', '7': '2', '8': '1', 
          '9': '0', ' ': ' '}
pontuacoes = "!?.,;:'\"()-"

def codificar_atbash():
    while True:
        texto = input('Digite uma palavra para a codificação em Atbash (ou "sair" para encerrar): ')

        if texto.strip() == "sair" or texto.strip() == "SAIR": 
            break            
        codigo = ""

        for letra in texto:
            if letra in atbash:
                codigo += atbash[letra]
            elif letra in pontuacoes:
                codigo += letra
            else:
                print(f'Aviso: "{letra}" não é uma letra válida e foi ignorada.')

        return(codigo)
            

atbash_invertido= {valor: chave for chave, valor in atbash.items()}

def decodifica_Atbash():
    while True:
        codigo = input('Digite o código em atbash ,(ou "sair" para encerrar): ')

        if codigo.strip() == "sair" or codigo.strip()=="SAIR":
            print("Encerrando...")
            break

        texto_final=[]
        codigo = codigo.strip()
        lista_palavras = codigo.split()
        for palavra in lista_palavras:
            texto=""
            for letra in palavra:
                try:
                    texto += atbash_invertido[letra]
                except KeyError:
                    print(f'Aviso: "{letra}" não é um caractere em atbash válido e foi ignorado.')
            texto_final.append(texto)
                


        return(" ".join(texto_final))

