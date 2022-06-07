"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
nome = input("Digite seu nome: ")
if len(nome) <= 4:
    print(f'Seu nome [ {nome} ] é muito curto, valor: [ {len(nome)} ]')
elif (len(nome) > 6 and len(nome) <= 8):
    print(f'Seu nome [ {nome} ] é Normal, valor: [ {len(nome)} ]')
else:
    print(f'Seu nome [ {nome} ] é muito grande, valor: [ {len(nome)} ]')
