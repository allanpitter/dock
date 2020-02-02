'''
dock14.py - Módulo OS (Sistema Operacional)
825-704-078
'''
# 1 - Criar um diretorio
import os
#os.mkdir('dir1')

# 2 - Excluir um diretorio
#os.rmdir('dir1')

# 3 - Listar Arquivos
'''
caminho = '/tmp'  # informar o diretorio/pasta especifica
#for arquivo in os.listdir(caminho):
for arquivo in os.listdir():
    print(arquivo)
'''
# 3.1 - Verificar a existencia de um arquivo no diretorio
'''
arquivo = open('arq3.txt','w')
arquivo.close()
for arquivo in os.listdir():
     if arquivo == 'arq3.txt':
         print("Encontrei:",arquivo)
'''

# 4 - Copiar um Arquivo
'''
import shutil
arquivo = open('arqnovo.txt','w')
arquivo.close()
shutil.copyfile('arqnovo.txt','arqdest.txt')
'''
# 5 - Renomear um Arquivo
#import os, shutil
#os.rename('arqdest.txt','arqnovo2.txt')

# 6 - Excluir um Arquivo
import os
os.remove('arqnovo2.txt')





