# [J]efferson , Eng. De Produção
nomes1 = ['jefferson', 'jonas', 'herverton']
nomes2 = ['rayssa', 'juliana', 'doguinho']

junta_nomes = zip(nomes1, nomes2)

for par1, par2 in junta_nomes:
    print(f'{par1.capitalize()} e {par2.capitalize()}')
