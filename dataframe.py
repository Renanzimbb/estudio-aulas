import pandas as pd

dados = [['Julio', 30], ['Renan', 35], ['Maria', 20]]
df = pd.DataFrame(dados,columns=['Nome', 'idade'])
print(df)
print('--' * 20)

dicionario = {'Nome2': ['Maria', 'João', 'Pedro'], 'Idade': [10,20,30]}
df2 = pd.DataFrame(dicionario)
print(df2)
print('--' * 20)

df3 = pd.read_excel('vendas_julho.xlsx')


df ['Idoso'] = df ['idade'] * 3
print(pd.pivot_table(df,index=['Nome']))


