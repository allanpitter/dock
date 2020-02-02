'''
dock11.py - Estrutura For (loop)
https://github.com/allanpitter/dock
718-588-156
'''
# Dados
empresa = 'dock'
lista   = [1,2,3,4,5]
tupla   = (2,4,6,8,10)
dicionario = {'Produto1':10,'Produto2':50}
d = {'a':1,'a':2}
# print(d)

# Ex1
'''
for letra in empresa:
    print(letra,end='')  # Exibe o '-' entre as letras: d-o-c-k-
print()
for x in empresa:
    print(x,end='\t') # Exibe as letras com tabulação d o c k
print()
for n in empresa:
    print(n,end='\n') # Exibe cada letra em uma linha

print('dado1','dado2',sep='---')
'''

#Ex2
'''
lista = [1,2,3,4,5]
for numero in lista:
    print(numero,end=',')
print()

tupla = (2,4,6,8,10)
for numero in tupla:
    print(numero,end=',')
'''
#Ex3
'''
lista = [2,4,6]
soma = 0
for abacaxi in lista:
    soma = soma + abacaxi
    print("Valor do Abacaxi:",abacaxi,"Vl.soma:",soma)
print("O total é:",soma)
print("A soma total é:",sum(lista))
'''
#Ex4 - Tabuada
# for(i=0;i++;i<=10) algo similar em outras linguagens de programacao
'''
print("Tabuada com FOR")
for n in range(1,11):
    print(8,'X',n,'=',8*n)

print()
print("Tabuada com WHILE")
n=1
while n<=10:
    print(8,'X',n,'=',8*n)
    n+=1  # n=n+1
'''
# Ex5
'''
for letra in 'palavra':
    if letra == 'v':
        break
    print(letra)
print(' ')

for letra in 'palavra':
    if letra == 'v':
        continue
    print(letra)
'''
# Ex6
dicionario = {'Produto1':10,'Produto2':50}
for d in dicionario:
    print(d)

print()
for d in dicionario.items():  # par de chaves ('Produto1',10)
    print(d)

print()
for d in dicionario.values():  # exibe os valores 10 50
    print(d)

print()
for chave,valor in dicionario.items():  
    print('Chave:',chave,' - Valor:',valor)
    # Chave: Produto1 - Valor:10
    # Chave: Produto2 - Valor:50




















