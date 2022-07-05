# [J]efferson de Almeida Eng.Produção.
meuDict = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd'
}
print(meuDict)
for i in meuDict:
    print(i, meuDict[i])
# Aqui só funcuina se na função pop você passar a chave!
meuDict.pop(4)
print(meuDict)