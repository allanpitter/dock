"""
dock9.py - somando numeros
"""
print("Somar Números")
numero = 1
guardar_soma = 0
while numero > 0:
    print("Valor de guardar_soma:",guardar_soma)
    numero = int(input("Digite um Numero (0 p/ Finalizar):"))
    print("Valor de guardar_soma:",guardar_soma)
    guardar_soma = guardar_soma + numero
    print("Valor de guardar_soma:",guardar_soma)
    print(" ")
else:
    print("Terminei a execução")

print("A soma é:",guardar_soma)



