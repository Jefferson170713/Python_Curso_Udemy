"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
cpf = '12345678912'
cont = 0
vr = 0
# nessa primeira parte precisa ter algo para verificar se o cpf fornecido realmente só existe números
for i in range(9):
    vr = int(cpf[i])
    cont += (vr * vr)
resto = cont % 11
div = cont / 11
print(cont)
print(div)
print(resto)
pass