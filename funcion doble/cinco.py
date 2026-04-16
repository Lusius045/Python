def Doble(concat):
    i = 0
    for i in range(2):
        print(concat)

def concatenar(fraseA,fraseB):
    concat = fraseA+fraseB
    return concat

fraseA = input()
fraseB = input()
concat = concatenar(fraseA,fraseB)
Doble(concat)