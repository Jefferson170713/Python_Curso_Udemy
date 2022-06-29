"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
import func_dentro_de_func_exer01

def nome():
    a = 'Jefferson, '
    return a
def sonho_luta():
    lt = nome() + 'você vai conseguir seus sonhos '
    return lt
def acreditar_persistir():
    ap = sonho_luta() + ", continue a trabalhar duro! stay hard!!!"
    return ap
var = acreditar_persistir()
print(var)
print(type(nome()))
testando_import = func_dentro_de_func_exer01.func_1() # Descobrir que posso passar programas
testando_import_2 = func_dentro_de_func_exer01.func_2(func_dentro_de_func_exer01.func_1()) # muito legal
print(testando_import)
print(testando_import_2)