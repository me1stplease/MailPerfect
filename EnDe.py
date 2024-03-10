import random


def keyGen(al):
    temp = al.copy()
    random.shuffle(temp)
    return temp


def encrypt(al, key, text):
    encryptedText = ''
    for char in text:
        if char not in al:
            encryptedText += char
        else:
            index = al.index(char)
            # print(char+" IN : " + str(index))
            encryptedText += key[index]
    return encryptedText


def decrypt(al, key, text):
    decryptedText = ''
    for char in text:
        if char not in al:
            decryptedText += char
        else:
            index = key.index(char)
            decryptedText += al[index]

    return decryptedText


# def ende(inputText,k):
#     # inputText = 'My name is Mahtab Alam'

#     # k = keyGen(alpha)

#     enc = encrypt(alpha, k, inputText)
#     dec = decrypt(alpha, k, enc)
#     print(enc)
#     print(dec)
