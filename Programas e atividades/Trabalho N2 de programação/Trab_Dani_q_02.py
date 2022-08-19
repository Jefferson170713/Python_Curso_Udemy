# [J]efferson , Eng. De Produção

saldo = float(input('Qual valor foi depositado? = '))

meses = int(input('Quantos meses irá render? = '))

for rendimento in range(meses):
    saldo += (saldo * 0.01)

print(f'\nSeu Saldo após {meses} meses é de = R${saldo:.2f}')