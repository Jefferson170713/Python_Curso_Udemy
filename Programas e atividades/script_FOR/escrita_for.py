"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
nome = 'Jefferson de almeida'
print(nome, ' tipo: ', type(nome))
n = nome.split()
print(n)
m = '$'.join(n)
print(m)
for i in range(5):
    for j in range(i):
        print("*", end='.')
    print(' ')
print("#######################")
for i in range(5,1,-1):
    for j in range(i-1):
        print("*", end='.')
    print(' ')