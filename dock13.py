'''
dock13.py
Modulo OS - Sistema Operacional
- Criar um diretorio
- Apagar um diretorio
- Copiar um arquivo
- renomear um arquivo
- listar arquivos
'''
import os
diretorio = 'c:/caminho/'
# 1 - criar um diretorio
#os.mkdir(caminho,'diretorio1')
# 2 - apagar um diretorio
#os.rmdir('diretorio1')
# 3 - Lista arquivo
for arquivo in os.listdir():
    #print(arquivo)
    if arquivo == 'arq3.txt':
        print(arquivo)
        print('Arquivo Existe')
        x = open(arquivo,'r')
        for dado in x.readlines():
            #if 'dado2' in dado:
            if dado == 'dado2\n':
                print(dado)


    
