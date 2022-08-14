# [J]efferson , Eng. De Produção
"""
    Um engenheiro elaborou uma lista com faixas de resistência mecânica de tipos de ferro
    usados na construção de elementos estruturais que frequentemente precisa ser
    consultada, conforme a tabela abaixo. Elabore um programa que, ao receber uma
    identificação de faixa de resistência mecânica, sejam mostrados na tela a identificação
    e os valores extremos de resistência dessa faixa. O programa deve ser capaz de repetir
    a execução até que o valor &quot;0&quot; seja digitado. Caso a identificação informada não conste
    da tabela, a mensagem “Não consta da tabela” deve ser exibida e o programa fica à
    espera de um novo valor de faixa:
"""
def mostra_tabela():
    print("""
              RESISTÊNCIA MECÂNICA
    -----------------------------------------
    |   FAIXA   |      DE     |     ATÉ     |
    -----------------------------------------
    |     1     |   10 kg/cm² | 50 kg/cm²   |
    |     2     |   51 kg/cm² | 100 kg/cm²  |
    |     3     |  101 kg/cm² | 150 kg/cm²  |
    |     4     |  151 kg/cm² | 200 kg/cm²  |
    |     5     |  201 kg/cm² | 250 kg/cm²  |
    -----------------------------------------
    """)
def faixa(a, b):
    if 10 <= b <= 50:
        print(f"""
                   RESISTÊNCIA MECÂNICA
        -----------------------------------------
        |   FAIXA   |      DE     |     ATÉ     |
        -----------------------------------------
        |     {a}     |  10 kg/cm²  |  50 kg/cm²  |
        -----------------------------------------
        """)
    elif 51 <= b <= 100:
        print(f"""
        RESISTÊNCIA MECÂNICA
        -----------------------------------------
        |   FAIXA   |      DE     |     ATÉ     |
        -----------------------------------------
        |     {a}     |  51 kg/cm²  |  100 kg/cm² |
        -----------------------------------------
        
        Valor selecionado: {b} kg/cm²
       """)
    elif 101 <= b <= 150:
        print(f"""
        RESISTÊNCIA MECÂNICA
        -----------------------------------------
        |   FAIXA   |      DE     |     ATÉ     |
        -----------------------------------------
        |     {a}     |  101 kg/cm² |  150 kg/cm² |
        -----------------------------------------

        Valor selecionado: {b} kg/cm²
         """)
    elif 151 <= b <= 200:
        print(f"""
        RESISTÊNCIA MECÂNICA
        -----------------------------------------
        |   FAIXA   |      DE     |     ATÉ     |
        -----------------------------------------
        |     {a}     |  151 kg/cm² |  200 kg/cm² |
        -----------------------------------------

        Valor selecionado: {b} kg/cm²
         """)
    elif 201 <= b <= 250:
        print(f"""
        RESISTÊNCIA MECÂNICA
        -----------------------------------------
        |   FAIXA   |      DE     |     ATÉ     |
        -----------------------------------------
        |     {a}     |  201 kg/cm² |  250 kg/cm² |
        -----------------------------------------

        Valor selecionado: {b} kg/cm²
        """)
    else:
        print(f"""
        RESISTÊNCIA MECÂNICA
        -----------------------------------------
        |   FAIXA   |      DE     |     ATÉ     |
        -----------------------------------------
        |    {a}    |  201 kg/cm² | 250 kg/cm²  |
        -----------------------------------------

        Valor selecionado: {b} kg/cm²
        """)
validador = bool(True)
id = int()

while validador == True:
    mostra_tabela()
    valor = int(input('Digete um valor de resistência: '))
    if valor > 250:
        print('Por favor, Digite somente a faixa de valores da tabela.')
        continue
    elif 201 <= valor <= 250:
        id = 5
        faixa(id, valor)
        validador = False
    elif 151 <= valor <= 200:
        id = 4
        faixa(id, valor)
        validador = False
    elif 101 <= valor <= 150:
        id = 3
        faixa(id, valor)
        validador = False
    elif 51 <= valor <= 100:
        id = 2
        faixa(id, valor)
        validador = False
    elif 10 <= valor <= 50:
        id = 1
        faixa(id, valor)
        validador = False
    else:
        var = int(input("Se deseja sair, digite 0: "))
        if var != 0:
            continue
        validador = False


