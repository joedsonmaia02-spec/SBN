def codificar_ascii(texto_de_entrada):
    texto_em_ascii=[]
    for letra in texto_de_entrada:
        if letra==" ":texto_em_ascii.append(32)
        texto_em_ascii.append(ord(letra))
        print(texto_em_ascii)
        print(texto_de_entrada)
    return (" ".join(map(str,texto_em_ascii)))


        
        