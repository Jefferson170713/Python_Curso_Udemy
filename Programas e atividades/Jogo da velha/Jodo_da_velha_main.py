# [J]efferson , Eng. De Produção
import Jogo_da_velha_func
jogo = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]
jogador1 = 'Jefferson'
jogador2 = 'Robert J'
linha = 0
coluna = 0
simbolo1 = str('%')
simbolo2 = str('*')

#jogo = Jogo_da_velha_func.gameStart(jogo)
#print(jogo)
#print()
#Jogo_da_velha_func.mostra_jogo(jogo)
simbolo1 = Jogo_da_velha_func.recebe_simolo(simbolo1, simbolo2, jogador1)
print(simbolo1)
