print("Equação do Segundo Grau")
print("--------------------------")
valorA = int(input("Informe o valor de A: "))
valorB = int(input("Informe o valor de B: "))
valorC = int(input("Informe o valor de C: "))
print("--------------------------")
delta = (valorB * valorB) -4*valorA*valorC
print("O valor de Delta: ", delta)
print("---------------------------")
if delta < 0:
    print("Para todo Delta negativo, não existe raizes reais")
elif delta == 0:
    x1 = (-valorB + (delta**0.5)/2*valorA)
    print("Para todo delta zero, temos duas raizes iguais a", x1)
    x1 = (-valorB + (delta**0.5)/2*valorA)
    x2 = (-valorB - (delta**0.5)/2*valorA)
    print("Para todo delta positivo. Raizes diferentes: ")
    print("x' = ", x1)
    print("x'' = ", x2)
    
        


