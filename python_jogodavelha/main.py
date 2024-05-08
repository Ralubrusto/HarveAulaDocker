import random

# Opções de jogada: 'PEDRA', 'PAPEL', 'TESOURA'
JOGADAS_VALIDAS = ['PEDRA', 'PAPEL', 'TESOURA']


def calcula_resultado_jogo_da_velha(jogada_jogador, jogada_adversario):
    if jogada_jogador == jogada_adversario:
        return 'Empate'
    elif jogada_jogador == 'PEDRA':
        if jogada_adversario == 'PAPEL':
            return 'Derrota'
        else:
            return 'Vitória'
    elif jogada_jogador == 'PAPEL':
        if jogada_adversario == 'TESOURA':
            return 'Derrota'
        else:
            return 'Vitória'
    elif jogada_jogador == 'TESOURA':
        if jogada_adversario == 'PEDRA':
            return 'Derrota'
        else:
            return 'Vitória'


## INÍCIO DO SCRIPT DE EXECUÇÃO

# Coletando dados iniciais do jogador
nome_jogador = input("Olá, digite seu nome: ")
print(f"Muito prazer, {nome_jogador}! Vamos jogar uma partida de jogo da velha!")

# Solicitando uma jogada. O código só continuará quando uma entrada válida for inserida
jogada_jogador = input("Insira sua jogada (PEDRA, PAPEL, TESOURA): ").strip().upper()

while jogada_jogador not in JOGADAS_VALIDAS:
    print(f"Jogada inválida! Você digitou {jogada_jogador}, mas as opções válidas são {JOGADAS_VALIDAS}")
    jogada_jogador = input("Insira uma jogada válida (PEDRA, PAPEL, TESOURA): ").strip().upper()


jogada_computador = random.choice(JOGADAS_VALIDAS)

resultado = calcula_resultado_jogo_da_velha(jogada_jogador, jogada_computador)

print(f"Você jogou: {jogada_jogador}")
print(f"O computador jogou: {jogada_computador}")
print(f"Resultado: {resultado}")


