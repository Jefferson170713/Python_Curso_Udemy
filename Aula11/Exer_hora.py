"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
# o programa vai pedir um valor entr 0 e 24 e o programa irá dizer, bom dia, boa tarde ou boa noite.
try:
    h = int(input("Digite o valor da hora: "))
    min = int(input("Digite o valor dos minutos: "))

    if ((h > 0) and (h < 24)) and ((min > 0) and (min < 60)):
        if (h > 0) and (h < 11):
            print(f"Bom dia!!!")
            print(f'Hora [{h}], min [{min}]', end='.')
        elif (h > 11) and (h < 17):
            print(f"Boa Tarde!!!")
            print(f'Hora [{h}], min [{min}]', end='.')
        else:
            print(f"Boa Noite!!!")
            print(f'Hora [{h}], min [{min}]', end='.')
    else:
        print(f'A hora não é válida!')
except:
    print(f'Você não digitou um Número!')
