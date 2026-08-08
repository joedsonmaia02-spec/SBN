from dict import import_dicionario

text = "hfsxfit"


def quebrar_cifra():
    chave = 0
    dicionario = import_dicionario()
    test_word = ""
    while True:
        for word in text.split():
            if test_word in dicionario["palavras"]:
                return 26-(chave-1)
            test_word=""
            for i in range(len(word)):
                shifted_character = chr((ord(word[i]) - ord('a') + chave) % 26 + ord('a'))
                test_word += shifted_character
                print(test_word)

        chave = chave + 1

print(quebrar_cifra())
