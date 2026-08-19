from dict import import_dicionario


def quebrar_cifra(text):

    chave = 1
    dicionario = import_dicionario()
    test_word = ""



    while chave<=26:
        for word in text:
            if test_word in dicionario["palavras"]:
                if len(text)==1:return 26-chave +1
                else:return 26-chave

            test_word=""

            for i in range(len(word)):
                shifted_character = chr(  ((( ord(word[i]) - ord('a') ) + chave)%26 ) + ord('a')  )
                test_word += shifted_character
                print(test_word)

        chave = chave + 1

    return None
