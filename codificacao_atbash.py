atbash = {'A':'Z','B':'Y','C':'X','D':'W','E':'V','F': 'U', 
          'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 
          'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 
          'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G', 'U': 'F', 
          'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A',
          '0': '9', '1': '8', '2': '7', '3': '6', '4': '5', 
          '5': '4', '6': '3', '7': '2', '8': '1', '9': '0', 
          ' ': ' '}
def codificaAtbash():
    while True:
        texto = input('Digite uma palavra (ou "sair" para encerrar): ').upper()

        if texto == "SAIR": 
            break            
        codigo = ""

        for letra in texto:
            codigo = codigo + atbash.get(letra, letra)
            
        print(codigo)