'''
dock18.py - Funcoes
'''
#1 - Anatomia de uma funcao
#    print  (        "Ola Mundo"     )
#    ------ --       -----------    ---
#    funcao abertura parametro(s)   fechamento
'''
a = 1
b = 2
print(a+b)

def soma(n1, n2):
    print('Valor N1:',n1)
    print('Valor N2:',n2)
    return n1+n2

print(soma(2,5))
a = 6
b = 4
print(soma(a, b))

resultado = soma(7,4)
print(resultado)
'''
#ex2 


def subtrair(n1, n2):
    return n1-n2

def multiplicacao(n1, n2):
    return n1*n2

def divisao(n1, n2):
    try:
        return n1/n2
    except:
        print("Você informou um número errado em N2")

def exibir(f,nome='Usuario(a)'):
    print(f,nome)

def soma(n1, n2):
    return n1+n2

def calculadora(op,v1,v2):
    return op(v1,v2)

def calculatudo(x1,x2):
    return x1+x2, x1*x2, x1-x2, x1/x2

print("Resultado:",calculatudo(10,3))

#print(calculadora(soma,3,4))
#print(soma(3,4))

# def exibir(f,nome='Usuario(a)',b): # não pode fazer isso
'''
x = 10
y = 2
print("Resultado Adição:",soma(x,y))
print("Resultado Subtração:",subtrair(x,y))
print("Resultado Multiplicação:",multiplicacao(x,y))
print("Resultado Divisão:",divisao(x,y))
print("Resultado Divisão:",divisao(10,0))
exibir('Ola')
'''



    
