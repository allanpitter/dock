'''
dock17.py - ler uma planilha
pip install xlrd
https://github.com/allanpitter/dock
'''
import pandas as pd
df = pd.read_excel('despesas01.xlsx')
print(df)

print("Cabeçalho")
print(df.columns)
print(df['Item'])

for i in df.index:
    print(df['Valor'][i])
    #lista['Valor'][2]











