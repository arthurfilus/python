import random

print('Sejam bem-vindos ao Zombie Dice\n')

num_jog = int(input('Informe o número de jogadores: '))

if 0 < num_jog < 2:
    print('O jogo deve conter 2 ou mais jogadores')
    int(input('Informe o número de jogadores: '))
elif num_jog == 0:
    print('Não é possível jogar sem jogadores. Informe 2 ou mais jogadores.')
    int(input('Informe o número de jogadores: '))
else:
    print(f'Vocês jogarão em {num_jog} pessoas!\n')

jogadores = []
for i in range(num_jog):
    nome = input('Qual o nome do Jogador ' + str (i + 1) + '? ')

    jogadores.append(nome)
print(f'Os jogadores serão: {jogadores}\n')

dado_verde = 'PCCTPC'
dado_amar = 'TPCTPC'
dado_verm = 'TPTCPT'

dados = [
    dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde,
    dado_amar, dado_amar, dado_amar, dado_amar,
    dado_verm, dado_verm, dado_verm,
]

print('A matança vai começar e você vai ter que correr')

jog_da_rodada = 0
dado_sorteado = []
tiros = 0
passos = 0
cerebros = 0
cor_dado = 0

while:

    print('Rodada do jogador', jogadores[jog_da_rodada])

    for i in range(0,2):
        num_sort = random.randint(0,12)
        dado_sorteado = dados[num_sort]

    if dado_sorteado == 'PCCTPC':
        cor_dado = 'Verde'
    elif dado_sorteado == 'TPCTPC':
        cor_dado = 'Amarelo'
    else:
        cor_dado = 'Vermelho'

    print('Dado sorteado: ', dado_sorteado)

    dado_sorteado[i] == dado_sorteado

    print('As faces sorteadas foram: ')
