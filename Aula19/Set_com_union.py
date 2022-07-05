# [J]efferson , Eng. De Produção
# Set, Sets ou conjuntos em inglês
"""
        A maior diferença entre, sets, listas e dicionários é que os sets so suportão elementos de um mesmo conjuto.
    Sem falar que todo dicionário tem uma chave em específico
    add(adiciona), update(atualiza), clear, discard, union(uni) ou |
    intersection & (todos os elementos presentes nos dois sets)
    diference - (elementos apenas no set da esquerda)
    symmetric_diference(elementos que estão nos dois, mas não em ambos)
"""
s1 = set()
s1.add('Jefferson')
s1.add('Rayssa')
s1.add('Jonas')
s1.add('Alana')
s1.add('Allan')
s1.add('Herverton')
s1.add('Juliana')
s1.add('Robert')
s2 = {17, 13, 24, 36, 45,96, 'Robert'}
s3 = s2 | s1
print(s3)
s4 = s2 & s1
print(s4)
s5 = s2 ^ s1
print(s5)