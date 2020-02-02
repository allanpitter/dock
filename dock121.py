'''
dock12.py
Arquivo texto
'''
# 1 - Criar um arquivo
'''
arquivo = open('arq1.txt','w')
arquivo.close()
'''
# 2 - Adicionando um conteúdo
'''
arquivo = open('arq2.txt','w')
arquivo.writelines("Meu conteudo")
arquivo.close()
'''
# 3 - Adicionando multiplas linhas
'''
arquivo = open('arq3.txt','w')
linhas  = ['dado1','dado2','dado3']
arquivo.writelines(linhas)
arquivo.close()
'''
# 3 - Adicionando multiplas linhas
'''
arquivo = open('arq3.txt','w')
linhas  = ['dado1\n','dado2\n','dado3\n']
arquivo.writelines(linhas)
arquivo.close()
'''
#4 - Adicionando multiplas linhas
'''
arquivo = open('arq2.txt','a')
arquivo.writelines('Nova linha\n')
arquivo.close()
'''
#5 - definir um local/diretorio para gravar
'''
#forma 1 - Windows
arquivo = open('C:/Meus Documentos/pythondock/arq4.txt','w')
arquivo.close()
#forma 2 - Windows
arquivo = open('C:\\Meus Documentos\\pythondock\\arq5.txt','w')
arquivo.close() # \\novo diretorio
#forma 3 - Linux e Mac
#arquivo = open('/caminho/diretorio/arquiv5.txt','w')
#arquivo.close()
'''
#6 - Ler um arquivo
'''
arquivo = open('arq3.txt','r')
print(arquivo.readlines())
arquivo.close()

#6 - Ler um arquivo
arquivo = open('arq3.txt','r')
for linha in arquivo.readlines():
    print(linha)

#6 - Ler um arquivo
arquivo = open('arq3.txt','r')
for linha in arquivo.readlines():
    print(linha,end="")   
'''
#6 - Ler um arquivo
'''
arquivo = open('arq1.txt','r')
linha = arquivo.readline()
while linha != '':
    print(linha,end="")
    linha = arquivo.readline() # proxima linha
else:
    print('Não executou, arquivo vazio')
arquivo.close()
'''
# 7- Ler linha por linha
'''
arquivo = open('arq3.txt','r')
linha = arquivo.readline()
print('linha1:',linha)
linha = arquivo.readline()
print('linha2:',linha)
linha = arquivo.readline()
print('linha3:',linha)
arquivo.close()
'''
# 8 - Leitura com o declarador with
'''
with open("arq3.txt","r") as meu_arquivo:
    for linha in meu_arquivo.readlines():
        print(linha,end="") 

# 9  - Origem e Destinos
with open("arq3.txt","r") as origem,  open("a3.txt","w") as dest:
    for linha in origem.readlines():
        dest.write(linha)
'''
# 10 - Leitura a partir de uma posição
arquivo = open("arq3.txt","r")
print("primeira linha:",arquivo.readline())
arquivo.seek(13)
print("segunda linha:",arquivo.readline())
arquivo.close()

# 0123456789
# 1111.2222.3333.4444






