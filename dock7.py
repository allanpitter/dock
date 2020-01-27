"""
dock7.py - Leitura de Dados
"""
print("### Programa de Boas Vindas ###")

# Criando as variáveis
nome = input("Digite seu nome:")
idade = input("Digite a sua idade:")
# Exibindo os dados
print(nome, "Seja Bem-vindo(a)")
print("Você tem",idade,"anos")

idade = int(idade)  # int() converte um texto em numero

if   idade > 1   and idade <  18:
    print("Você é menor de Idade")
    print("Se cuida bebê")
elif idade >= 18 and idade <= 64:
     print("Você é maior de Idade")
elif idade >= 65:
    print("Você é da Melhor Idade")
else:
    print("Você digitou um valor invalido")
    
















