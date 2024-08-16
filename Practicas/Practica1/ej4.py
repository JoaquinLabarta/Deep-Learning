def calcular(p1,p2):
    import math
    dis = math.sqrt(((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2))
    return dis
    
def alternativa(p1,p2):
    import math
    return math.dist(p1,p2)

p1 = [5,3]
p2 = [2,1]
print(calcular(p1,p2))
print(alternativa(p1,p2))