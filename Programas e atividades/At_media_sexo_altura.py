"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
"""
Escrever um programa que leia altura e sexo de 15 pessoas. O programa deve calcular e apresentar:
- quantidade de homens no grupo
- altura média das mulheres
"""
med_t = float()
med_f = float()
med_m = float()
qtd_m = int()
qtd_f = int()
i = 1
while i <= 3:
    sex = str(input("Digite m(masculino) ou f(Feminino): "))
    alt = float(input("Digite a altura: "))
    if sex == 'm':
        qtd_m += 1
        med_t += alt
        med_m += alt
    else:
        qtd_f += 1
        med_t += alt
        med_f += alt
    i += 1
else:
    med_t = (med_t/3) # Cuidado ao dividir pela quantidade que a questão pede, mas se funciona para 3 ==> 15
    med_m = (med_m/qtd_m)
    med_f = (med_f/qtd_f)
    print("""
            Quantidade :   Masculino     Feminino
                15            [{}]          [{}]
            Média      :            [{:.2f}]
            Média de Mulheres:      [{:.2f}] 
            Média de Homens:        [{:.2f}]
    """.format(qtd_m, qtd_f, med_t, med_f, med_m))