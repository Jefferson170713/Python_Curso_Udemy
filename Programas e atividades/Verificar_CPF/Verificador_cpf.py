"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
# Fonte de referência de apoio: https://www.macoratti.net/alg_cpf.htm <-- pesquisa
Smd = 0 #Acumulador
n = 10 #Parte da multiplicação decrescente
vrf = 0 #Número verificador
rest_d = 0 #Resto da divisão
vrf_rpt = True # verificação de repetição do programa principal
while vrf_rpt:
    cpf = input("Digite o cpf: ")  # Aqui, como é Stringo, aceita qualquer dado inserido
    if (len(cpf) == 11) and (cpf.isnumeric()):  # primeiro etapa de verificação do código
        for i in range(9):  # 2 Função verificadora do primeiro dígito
            Smd += (n * int(cpf[i]))  ##2 Passando a posiçao da String cpf para inteiro
            n -= 1
        rest_d = (Smd % 11)
        if rest_d < 2:
            vrf = 0
            if vrf == int(cpf[9]):
                print(f'O PRIMEIRO dígito verificador do cpf: {cpf} é Válido!!!')
                #print('etapa 1')
            else:
                print("O Cpf não é válido!!!")
                print('Por favor, INSIRA um CPF VÁLIDO!!!')
                print(f'Este {cpf} não é!')
                #print('Etapa 2')
        else:
            vrf = 11 - (Smd % 11)
            if vrf == int(cpf[9]):
                print(f'O PRIMEIRO dígito verificador do cpf: {cpf} é Válido!!!')
                #print('etapa 3')
            else:
                print("O Cpf não é válido!!!")
                print('Por favor, INSIRA um CPF VÁLIDO!!!')
                print(f'Este {cpf} não é VÁLIDO!')
                #print('etapa 4')
        n = 11
        Smd = 0
        for i in range(10):
            Smd += (n * int(cpf[i]))
            n -= 1
        rest_d = (Smd % 11)
        if rest_d < 2:
            if vrf == int(cpf[10]):
                print(f'O SEGUNDO dígito verificador do cpf: {cpf} é Válido!!!')
                #print('etapa 5')
            else:
                print("O Cpf não é válido!!!")
                print('Por favor, INSIRA um CPF VÁLIDO!!!')
                print(f'Este {cpf} não é!')
                #print('Etapa 6')
        else:
            vrf = 11 - (Smd % 11)
            if vrf == int(cpf[10]):
                print(f'O SEGUNDO dígito verificador do cpf: {cpf} é Válido!!!')
                #print('etapa 7')
            else:
                print("O Cpf não é válido!!!")
                print('Por favor, INSIRA um CPF VÁLIDO!!!')
                print(f'Este {cpf} não é VÁLIDO!')
                #print('etapa 8')
    else:
        print("O CPF Digitado não é VÁLIDO!!!\n")
    resposta_p = input("Digite s(sim) para repetir o programa ou n(não) para sair. ")
    if (resposta_p == 's') or (resposta_p == 'S'):
        continue
    elif (resposta_p == 'n') or (resposta_p == 'N'):
        vrf_rpt = False
    else:
        print("POR FAVOR, DIGITE APENAS 'S'/'s' OU 'N'/'s'.\n")
        vrf_rpt_2 = True
        while vrf_rpt_2:
            resposta_p = input("Digite s(sim) para repetir o programa ou n(não) para sair. ")
            if (resposta_p == 's') or (resposta_p == 'S'):
                vrf_rpt_2 = False
            elif (resposta_p == 'n') or (resposta_p == 'N'):
                vrf_rpt = False
                vrf_rpt_2 = False
            else:
                print("POR FAVOR, DIGITE APENAS 'S'/'s' OU 'N'/'s'.\n")
else:
    print("Muito obrigado por rodar o programa!")
