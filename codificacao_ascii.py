def codificar_ascii(texto_de_entrada):
    texto_em_ascii=[]
    for letra in texto_de_entrada:
        if letra==" ":texto_em_ascii.append(32)
        texto_em_ascii.append(ord(letra))
    return (" ".join(map(str,texto_em_ascii)))

def decodificar_ascii(texto_em_ascii):
    texto_de_saida=""
    for letra in texto_em_ascii.split():
        texto_de_saida+=chr(int(letra))
    return texto_de_saida