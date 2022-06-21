"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
# Objetivo, criar um program que escreva em ordem crescente e decrescente ao mesmo tempo
# Tanto com o laço for como o laço if

cont1 = 10
cont2 = 0
valid = True
print("Primeiro com o laço While!")

while valid:
    print(f"Contador 1 [{cont1}] e Contador 2 [{cont2}]")
    cont1 -= 1
    cont2 += 1
    if cont1 == 0 and cont2 == 10:
        valid = False
print("Agora com o laço for!")
# uma possível solução seria com a função enumerate junto com a função range regressiva
for i, u in enumerate(range(11, 1, -1)):
    print(i + 1, u - 1)
