def open_file_read(path):
    lista_palavras=[]
    while True:
        try:
            with open(path, "r") as text_dump:
                text = text_dump.read()
                for word in text.split():
                    lista_palavras.append(word)
            return lista_palavras
        except:
            print("Erro ao abrir arquivo, tente novamente...")
            path=receber_path()


def receber_path():
        path=input("Insira o camhinho do arquivo: ")
        return path

def criar_lista_entrada(text):
    lista_palavras=[]
    for word in text.split():
        lista_palavras.append(word)
    return lista_palavras