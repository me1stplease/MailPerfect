

def encpi(text,replacable,replacing):
    temp = text
    for i in range(len(replacable)):
        temp = temp.replace(str(replacable[i]),str(replacing[i]))
    return temp