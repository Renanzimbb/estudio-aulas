import pandas as pd

df2 = pd.read_excel('buy-bybit.xlsx')
del df2['Order No.']
df2['Time'] = pd.to_datetime(df2['Time']).dt.date


df2['Fiat Amount'] = df2['Fiat Amount'].str.replace('BRL|,', '', regex=True).astype(float)
df2['Coin Amount'] = df2['Coin Amount'].str.replace('USDT|,', '', regex=True).astype(float)
soma_fiat_amount = df2['Fiat Amount'].sum()
soma_coin_amount = df2['Coin Amount'].sum()
media = soma_fiat_amount / soma_coin_amount
print('--' * 20)
print("Somatório da coluna Fiat Amount(Saído da conta):", soma_fiat_amount)
print("Somatório da coluna Coin Amount(usdt recebido:", soma_coin_amount)
print("Média do preço pago por dólar:", media)


