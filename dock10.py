"""
dock10 - While
"""
print("Contador")

numero = 0
while True:

    if numero == 4:
        numero +=1
        continue
    
    print("Contando:",numero)
    numero = numero + 1
   
    
    if numero > 10:
        break
