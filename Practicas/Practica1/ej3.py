def funcion(lista):
    lista2 = []
    for i in lista:
        if not i in lista2:
            lista2.append(i)
    return lista2

def alternativa(lista):
    return list(set(lista))

lista = [1,2,3,1,3,2,4,5,2,3,6]
print(alternativa(lista))