
# [J]efferson , Eng. De Produção

# 0 = Tentativa de Subir com o Elevador (Botão de Subir)
lim_elev = float(input('Digite o Limite de Carga do Elevador = '))
print(f'Limite de Carga do Elevador é de {lim_elev}Kg')

# peso = Peso do Elevador
peso = 0

while True:
    # carga = Carga Colocada no Elevador
    carga = float(input('Digite a carga a ser colocada no elevador = '))

    if carga == 0:
        break

    else:
        peso += carga
        print(f'Carga de {carga}Kg Adicionada (Total de Peso = {peso}Kg)')

if peso <= lim_elev:
    print(
        f'\nSubida do Elevador Autorizada!!\nCarga Total = {peso}Kg\nLimite de Carga = {lim_elev}Kg\nPeso Livre {lim_elev-peso}Kg')

else:
    print(
        f'\nSubida do Elevador Não Autorizada!!\nCarga Total = {peso}Kg\nLimite de Carga = {lim_elev}Kg\nAcima do Peso {peso-lim_elev}Kg')