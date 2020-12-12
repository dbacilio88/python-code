#sentence = "rUns dOg"

def operacion(sentence):

    palabra =[]
    for i in sentence:
        if(i== i.lower()):
            palabra.append(i.upper())
        elif i == i.upper():
            palabra.append(i.lower())

    #print(palabra)
    letra = ''.join(str(x) for x in palabra)
    invertir = letra.split(sep=" ")
    
    l = []

    for i in invertir:
        l.append(i+ ' ')
    
    l.reverse()
    letra = ''.join(str(x) for x in l)
    return letra

oracion = "aWESOME is cODING"
#oracion = "rUns dOg"
data = operacion(oracion)
print(data)