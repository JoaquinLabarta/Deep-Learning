lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]

def imprimir(lista1,lista2):
    for i,j in zip(lista1,lista2):
        print(i , j)

imprimir(lista1,lista2)