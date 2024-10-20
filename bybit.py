import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('vendas_julho.xlsx')
# Verificar as primeiras linhas do DataFrame para entender a estrutura
df = df.dropna() #dropa linhas vazias
del df['Status'], df['Transaction Fees'], df['Order No.']
df['Time'] = pd.to_datetime(df['Time']).dt.date

print(df.head())
df['Fiat Amount'] = df['Fiat Amount'].str.replace('USD', '').astype(float)
df['Coin Amount'] = df['Coin Amount'].str.replace('USDT', '').astype(float)
soma_fiat_amount = df['Fiat Amount'].sum()
soma_coin_amount = df['Coin Amount'].sum()
#print(df)
print('--' * 20)
print("Somatório da coluna Fiat Amount(crédito em conta):", soma_fiat_amount)
print("Somatório da coluna Coin Amount:", soma_coin_amount)
lucro = soma_fiat_amount - soma_coin_amount

# Calcular o percentual
percentual = (lucro / soma_coin_amount) * 100
print(f'Valor Investido: ${soma_coin_amount:.0f} USD, Retorno: {percentual:.2f}% / ${lucro:.2f}')

print('--' * 20)

result = df.groupby('Price').agg(
    occurrences=('Price', 'size'),
    total_coin_amount=('Coin Amount', 'sum')
).reset_index()
print(result)

result = df.groupby('Time').agg(
    total_coin_amount=('Coin Amount', 'sum'),
    total_fiat_amount=('Fiat Amount', 'sum'),
).reset_index()
result['Lucro'] = (result['total_fiat_amount'] - result['total_coin_amount']).round(2)
result['%'] = ((result['Lucro'] / result['total_coin_amount']))*100
media = result['Lucro'].mean()
print(result)
print(f'Média de Ganhos por dia: {media:.2f}')

#plt.title('Análise Diária de Lucro')
#plt.bar(result['Time'],result['Lucro'], label='Lucro no Dia')
#plt.scatter(result['Time'],result['Lucro'], color='Red', label='Lucro Máximo do Dia')
#plt.legend()
#plt.xlabel('Dia')
#plt.ylabel('Lucro')
#plt.show()


