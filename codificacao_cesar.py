alfabeto = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

def codificar_cesar(texto, deslocamento=1):
    tamanho = len(alfabeto)
    resultado = ""

    for letra in texto:
        letra_encontrada = False
        
        for i in range(tamanho):
            if alfabeto[i] == letra:
                novo_indice = i + deslocamento * 2
                
                while novo_indice >= tamanho:
                    novo_indice -= tamanho
                while novo_indice < 0:
                    novo_indice += tamanho
                
                resultado += alfabeto[novo_indice]
                letra_encontrada = True
                break
        
        if not letra_encontrada:
            resultado += letra

    return resultado#codigo legal

def decodificar_cesar(texto, deslocamento):
 
    tamanho = len(alfabeto)
    resultado = ""

    for letra in texto:
        letra_encontrada = False

        for i in range(tamanho):

            if alfabeto[i] == letra:
                novo_indice = i - deslocamento * 2 

                while novo_indice >= tamanho:
                    novo_indice -= tamanho  #Quando for maior que o alfabeto volta para o inicio
                    
                while novo_indice < 0:      #Como é capaz de ficar menor que 0 que é o inicial do alfabeto, soma o novo valor do indice ao tamanho
                    novo_indice += tamanho

                resultado += alfabeto[novo_indice]
                letra_encontrada = True
                break

        if not letra_encontrada:
            resultado += letra

    return resultado