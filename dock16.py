'''
dock16.py - criar um planilha excel
Módulo - xlsxwriter
Para instalar:
1 - Abrir um prompt de comando
2 - executar o comando: pip install xlsxwriter
'''
#Importar o Módulo xlsxwriter
import xlsxwriter

#Criar uma planilha(workbook) e uma aba(worksheet)
workbook = xlsxwriter.Workbook('despesas01.xlsx')
worksheet = workbook.add_worksheet()

#Criar alguns dados
despesas = (['Aluguel',1000],
            ['Gas',100],
            ['Ifood',400],
            ['Acad',50])

#Linha e Coluna inicial
row = 0
col = 0

#Criando os dados nas celulas
for item,custo in (despesas):
    worksheet.write(row,col,item)    # 0(linha), 0(coluna) = A1
    worksheet.write(row,col+1,custo) # 0(linha), 1(coluna) = B1
    row = row + 1

#formula
worksheet.write(row,0,"Total")
worksheet.write(row,1,"=SUM(B1:B4)")
workbook.close()


