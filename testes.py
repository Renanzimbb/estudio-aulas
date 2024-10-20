import pandas as pd

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

compras_totais_brl = soma_coin_amount_vendas * media_compras
vendas_totais_brl = soma_coin_amount_vendas * media


print('--' * 20)
print('Resumo Geral')
lucro = vendas_totais_brl - compras_totais_brl
imposto = lucro *.15
print(f'Lucro: R${lucro}')
print(f'Imposto a pagar: R${imposto}')
print('--' * 20)

print(compras_totais_brl)
print((vendas_totais_brl))