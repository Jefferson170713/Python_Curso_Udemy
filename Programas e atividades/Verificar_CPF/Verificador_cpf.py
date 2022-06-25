"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
cpf = '11144477735'#1 Aqui vou precisar fazer um tratamento
Smd = 0 #Acumulador
n = 10 #Parte da multiplicação decrescente
vrf = 0 #Número verificador
rest_d = 0 #Resto da divisão
print(len(cpf))
#-------------------------------------------------------------------------------------------
for i in range(9):#2 Função verificadora do primeiro dígito
    Smd += (n * int(cpf[i])) ##2 Passando a posiçao da String cpf para inteiro
    n -= 1
#-------------------------------------------------------------------------------------------
rest_d = (Smd % 11)
if rest_d < 2:
    vrf = 0
    print(f'{vrf} e {cpf[9]} 1111111\n\n')
    if vrf == int(cpf[9]):
        print(f'Soma das multiplicações: {Smd}')
        print(f'Valor do resto da divisão: {(Smd % 11)}')
        print(f'Valor do resto da divisão - 11: {11 - (Smd % 11)}')
        print(f'Resto da divisão: {rest_d}')
        print(f'Dígito 10 do cpf: {cpf[9]}')
        print(f'Dígito Verificador: {vrf}')
        print(1)

    else:
        print("O Cpf não é válido!!!")
        print('Por favor, INSIRA um CPF VÁLIDO!!!')
        print(f'Soma das multiplicações: {Smd}')
        print(f'Valor do resto da divisão: {(Smd % 11)}')
        print(f'Valor do resto da divisão - 11: {11 - (Smd % 11)}')
        print(f'Resto da divisão: {rest_d}')
        print(f'Dígito 10 do cpf: {cpf[9]}')
        print(f'Dígito Verificador: {vrf}')
        print(2)

else:
    vrf = 11 - (Smd % 11)
    print(f'{vrf} e {cpf[9]}\n\n')
    if vrf == int(cpf[9]):
        print(f'Soma das multiplicações: {Smd}')
        print(f'Valor do resto da divisão: {(Smd % 11)}')
        print(f'Valor do resto da divisão - 11: {11 - (Smd % 11)}')
        print(f'Resto da divisão: {rest_d}')
        print(f'Dígito 10 do cpf: {cpf[9]}')
        print(f'Dígito Verificador: {vrf}')
        print(3)

    else:
        print("O Cpf não é válido!!!")
        print(cpf[9])
        print(vrf)
        print(f'Soma das multiplicações: {Smd}')
        print(f'Valor do resto da divisão: {(Smd % 11)}')
        print(f'Valor do resto da divisão - 11: {11 - (Smd % 11)}')
        print(f'Resto da divisão: {rest_d}')
        print(f'Dígito 10 do cpf: {cpf[9]}')
        print(f'Dígito Verificador: {vrf}')
        print(4)
        pass

#-------------------------------------------------------------------------------------------
print('\n')
n = 11
Smd = 0
for i in range(10):
    Smd += (n * int(cpf[i]))
    n -= 1
rest_d = (Smd % 11)
if rest_d < 2:
    print(f'{vrf} e {cpf[10]} 1111111\n\n')
    if vrf == int(cpf[10]):
        print(f'Soma das multiplicações: {Smd}')
        print(f'Valor do resto da divisão: {(Smd % 11)}')
        print(f'Valor do resto da divisão - 11: {11 - (Smd % 11)}')
        print(f'Resto da divisão: {rest_d}')
        print(f'Dígito 10 do cpf: {cpf[10]}')
        print(f'Dígito Verificador: {vrf}')
        print(5)

    else:
        print("O Cpf não é válido!!!")
        print('Por favor, INSIRA um CPF VÁLIDO!!!')
        print(f'Soma das multiplicações: {Smd}')
        print(f'Valor do resto da divisão: {(Smd % 11)}')
        print(f'Valor do resto da divisão - 11: {11 - (Smd % 11)}')
        print(f'Resto da divisão: {rest_d}')
        print(f'Dígito 10 do cpf: {cpf[10]}')
        print(f'Dígito Verificador: {vrf}')
        print(6)
else:
    vrf = 11 - (Smd % 11)
    print(f'Soma das multiplicações: {Smd}')
    print(f'Valor do resto da divisão: {(Smd % 11)}')
    print(f'Valor do resto da divisão - 11: {11 - (Smd % 11)}')
    print(f'Resto da divisão: {rest_d}')
    print(f'Número do segundo Dígito validado: {cpf[10]}')
    pass
