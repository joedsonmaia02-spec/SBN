alfabeto_pos = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 
    'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 
    'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

lista_letras = list(alfabeto_pos.keys())

def codificaVigenere():
    while True:
        texto = input('Digite o texto (ou "sair" para encerrar): ').upper()
        if texto == "SAIR": 
            break            
            
        chave = input('Digite a palavra-chave: ').upper()
        if not chave:
            print("A chave não pode ser vazia.")
            continue
            
        codigo = ""
        indice_chave = 0

        for letra in texto:
    
            if letra in alfabeto_pos:
                letra_chave = chave[indice_chave % len(chave)]
                pos_chave = alfabeto_pos[letra_chave]
                
                pos_letra = alfabeto_pos[letra]
                
                nova_pos = (pos_letra + pos_chave) % 26
                
                codigo += lista_letras[nova_pos]

                indice_chave += 1
            else:
                codigo += letra
            
        print(f"Texto Cifrado: {codigo}\n")

if __name__ == "__main__":
    codificaVigenere()
