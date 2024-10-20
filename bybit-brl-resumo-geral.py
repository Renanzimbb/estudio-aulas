import pandas as pd

## DataFrame das Compras

df = pd.read_excel('buy-bybit.xlsx')
df = df.drop(81)

del df['Order No.']
df['Time'] = pd.to_datetime(df['Time']).dt.date

df['Fiat Amount'] = df['Fiat Amount'].str.replace('BRL|,', '', regex=True).astype(float)
df['Coin Amount'] = df['Coin Amount'].str.replace('USDT|,', '', regex=True).astype(float)
soma_fiat_amount_compras = df['Fiat Amount'].sum()
soma_coin_amount_compras = df['Coin Amount'].sum()
media_compras = soma_fiat_amount_compras/ soma_coin_amount_compras
print('--' * 20)
print('Resumo das Compras')
print('--' * 20)
print("Somatório da coluna Fiat Amount(Saído da conta):", soma_fiat_amount_compras)
print("Somatório da coluna Coin Amount(usdt recebido):", soma_coin_amount_compras)
print("Média do preço pago por dólar:", media_compras)


## DataFrame das Vendas

df2 = pd.read_excel('sell-bybit.xlsx')
del df2['Order No.']
df2['Time'] = pd.to_datetime(df2['Time']).dt.date

df2['Fiat Amount'] = df2['Fiat Amount'].str.replace('BRL|,', '', regex=True).astype(float)
df2['Coin Amount'] = df2['Coin Amount'].str.replace('USDT', '').astype(float)
soma_fiat_amount_vendas = df2['Fiat Amount'].sum()
soma_coin_amount_vendas = df2['Coin Amount'].sum()
media = soma_fiat_amount_vendas / soma_coin_amount_vendas
print('--' * 20)
print('Resumo das Vendas')
print('--' * 20)
print("Somatório da coluna Fiat Amount(crédito em conta):", soma_fiat_amount_vendas)
print("Somatório da coluna Coin Amount(usdt vendido):", soma_coin_amount_vendas)
print("Média do preço pago por dólar:", media)


print('--' * 20)
print('Resumo Geral')
lucro = soma_fiat_amount_vendas - soma_fiat_amount_compras
imposto = lucro *.15
print(f'Lucro: R${lucro}')
print(f'Imposto a pagar: R${imposto}')
print('--' * 20)