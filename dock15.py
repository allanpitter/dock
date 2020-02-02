'''
dock15.py - arquivos csv (arquivo com delimitadores)
dados.csv
Nome, Sobrenome, Vendas
Pedro, Silva, 3000
Maria, dos Santos, 5000
Ana, Maria, 8000
'''
# criar um arquivo exemplo nome dados.csv
'''
arquivo = open('dados.csv','w')
arquivo.writelines('Nome, Sobrenome, Vendas\n')
arquivo.writelines('Pedro, Silva, 3000\n')
arquivo.writelines('Maria, dos Santos, 5000\n')
arquivo.writelines('Ana, Maria, 8000\n')
arquivo.close()
'''
# 1 - Ler um arquivo csv
'''
import os,csv
#caminho = 'c:/diretorio'
#with open(os.path.join(caminho,'dados.csv'),'r') as meu_arquivo:
with open(os.path.join('dados.csv'),'r') as meu_arquivo:
    leitura = csv.reader(meu_arquivo)
    for linha in leitura:
        print(linha)
'''

# 2 - Ler um arquivo csv
import os,csv
with open(os.path.join('dados.csv'),'r') as meu_arquivo:
    leitura = csv.reader(meu_arquivo)
    next(leitura)
    for nome, sobrenome,salario in leitura:
        #print(f'Nome:{nome} Sobrenome:{sobrenome} - Valor:{vlvendas}')
        #print("Nome:",nome,"Valor:",float(salario))
        print(f'Nome:{nome} - Valor:{float(salario):12.8f}')
        






























