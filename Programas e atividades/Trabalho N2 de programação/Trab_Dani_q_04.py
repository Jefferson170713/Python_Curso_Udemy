# [J]efferson , Eng. De Produção

# Variáveis de Contagem de Ensaios Aprovados e Não Aprovados
var_ok = 0
var_n = 0

# 50 Ensaios Aleatórios para Teste de Air-Bag
for teste in range(50):
    tempo = float(input(f'Resultado do Teste {teste + 1} = '))
    print(f'Ensaio {teste + 1} de 50 = {tempo}ms')

    if tempo <= 30:
        var_ok += 1

    else:
        var_n += 1

# Verificar Porcentagem de Aprovados e Não Aprovados
print(f'{((100 * var_ok) / 50):.1f}% Ensaios Aprovados - De 50 ensaios, {var_ok} foram Aprovados!!'
      f'{((100 * var_n) / 50):.1f}% Ensaios Não Aprovados - De 50 Ensaios, {var_n} foram Reprovaodos!')