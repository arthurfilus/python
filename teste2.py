"""
Arthur Luiz Filus
Análise e Desenvolvimento de Sistemas
"""
import random
from random import randint

print('Sejam bem-vindos ao Zombie Dice\n')

num_jog = int(input('Informe o número de jogadores: '))  # int antes do input transforma uma str em número inteiro

while num_jog < 2:  # enquanto não houver 2 ou mais jogadors, nao irá dar acesso à proxima parte do jogo
    print('Não é possível jogar com menos de 2 pessoas. Informe um número maior que 2.\n')
    num_jog = int(input('Informe o número de jogadores: '))
else:  # a partir daqui, o jogo começa
    print(f'Vocês jogarão em {num_jog} pessoas.')

jogadores = []  # lista aberta para ser colocado o nome dos jogadores

for i in range(num_jog):  # função utilizada para abrir i vezes o input de nomes, utiliza num_jog como base de número
    nome = input('Qual o nome do Zumbi ' + str (i + 1) + '? ')

    jogadores.append(nome)  # função usada para jogar os nomes na lista aberta

print(f'Os zumbis do jogo serão: {jogadores}\n')

dado_verde = 'PCCTPC'  # criando os dados
dado_amar = 'TPCTPC'
dado_verm = 'TPTCPT'

dados = [  # todos os dados disponíveis em uma lista
    dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde,
    dado_amar, dado_amar, dado_amar, dado_amar,
    dado_verm, dado_verm, dado_verm,
]

print('A matança vai começar e você vai ter que correr')

jog_atual = 0
dado_sorts = []
tiros = 0
cerebros = 0
passos = 0
cor_dado = ''

def jogardados():
    for i in range(3):
        num_sort = random.randint(0, 12)
        dado_sort = dados[num_sort]

        if dado_sort == 'PCCTPC':
            cor_dado = 'verde'
        elif dado_sort == 'TPTCPT':
            cor_dado = 'vermelho'
        else:
            cor_dado = 'amarelo'

        print(f'O dado sorteado foi {cor_dado}')
        dado_sorts.append(dado_sort)

    return dado_sorts

def mostrardado():
    print('As faces do dado são: ', dado_sorts)

def inicializar(jog_atual):
    if jog_atual == num_jog - 1:
        jog_atual = 0
    else:
        jog_atual = jog_atual + 1

    dado_sorts = []
    tiros = 0
    cerebros = 0
    passos = 0

    if jog_atual == len(jogadores):
        print('Finalizando...')

def score(cerebros, tiros):
    print('Resultados da rodada: ')
    print('CÉÉÉÉÉÉÉÉÉÉBROS: ', cerebros)
    print('Tiros: ', tiros)

while True:
    print(f'Vez do zumbi {jogadores[jog_atual]}')


    """for i in range(3): 
        num_sort = random.randint(0, 12)
        dado_sort = dados[num_sort]

        if dado_sort == 'PCCTPC':
            cor_dado = 'verde'
        elif dado_sort == 'TPTCPT':
            cor_dado = 'vermelho'
        else:
            cor_dado = 'amarelo'

        print(f'O dado sorteado foi {cor_dado}')
        dado_sorts.append(dado_sort) """

    """print('As faces do dado são: ', jogardados())"""
    jogardados()
    mostrardado()

    for dado_sort in dado_sorts:
        sorteio = random.randint(0,5)
        face_dado = str(dado_sort[sorteio])

        if face_dado == 'C':
            print('Você comeu um CÉÉÉÉÉÉÉÉÉÉÉREBROOOO')
            cerebros += 1
        elif face_dado == 'T':
            print('Você levou um tiro. Vai morrer?')
            tiros += 1
        else:
            print('Sua vítima escapou HAHAHAHA')
            passos += 1

    """print('Resultados da rodada: ')
    print('CÉÉÉÉÉÉÉÉÉÉBROS: ', cerebros)
    print('Tiros: ', tiros)"""

    score(cerebros, tiros)

    if tiros < 3:
        if input('Você pretende continuar jogando? ') == 'n':
            """if jog_atual == num_jog - 1:
                jog_atual = 0
            else:
                jog_atual = jog_atual + 1

            dado_sorts = []
            tiros = 0
            cerebros = 0
            passos = 0

            if jog_atual == len(jogadores):
                print('Finalizando...')"""
            inicializar(jog_atual)
        else:
            print('Iniciando outra rodada')
            dado_sorts = []
    else:
        print('Você morreu!')
        break