# [J]efferson , Eng. De Produção
# Set, Sets ou conjuntos em inglês
"""
        A maior diferença entre, sets, listas e dicionários é que os sets so suportão elementos de um mesmo conjuto.
    Sem falar que todo dicionário tem uma chave em específico
    add(adiciona), update(atualiza), clear, discard, union(uni)
    intersection(todos os elementos presentes nos dois sets)
    diference(elementos apenas no set da esquerda)
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
print(f'O tamanho de Set1 é {len(s1)}')
print(s1)
for i in s1:
    print(i)
print(f'Agora o tamanho de Set1 é {len(s1)}')
s1.discard('Allan')
for i in s1:
    print(i)
print(f'Agora o tamanho de Set1 é {len(s1)}')