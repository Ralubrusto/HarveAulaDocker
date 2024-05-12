import random

# Opções de jogada: 'PEDRA', 'PAPEL', 'TESOURA'
JOGADAS_VALIDAS = ['PEDRA', 'PAPEL', 'TESOURA']


def calcula_resultado_jogo_pedrapapeltesoura(jogada_jogador, jogada_adversario):
    # Preencha a lógica aqui para o jogo de pedra papel tesoura.
    # Ele não precisa ter apenas 1 if, 1 elif e 1 else. A estrutura do jogo fica a seu critério
    if ...
        return 'Empate'
    elif :
        return 'Derrota'
    else:
        return 'Vitória'



## INÍCIO DO SCRIPT DE EXECUÇÃO

# Coletando dados iniciais do jogador
nome_jogador = input("Olá, digite seu nome: ")
print(f"Muito prazer, {nome_jogador}! Vamos jogar uma partida de pedra papel tesoura!")

# Solicitando uma jogada. O código só continuará quando uma entrada válida for inserida
jogada_jogador = input("Insira sua jogada (PEDRA, PAPEL, TESOURA): ").strip().upper()

# OPCIONAL - Inclua uma etapa de verificação se a jogada é válida ou não
# while ...:
    
# Configure aqui a jogada do compudator
# jogada_computador = 'PEDRA'   # Aqui é um caso de jogada fixa caso queira testar a lógica
jogada_computador = random.choice(JOGADAS_VALIDAS)   # Esse código aqui sorteia uma jogada para o computador aleatoriamente

resultado = calcula_resultado_jogo_pedrapapeltesoura(jogada_jogador, jogada_computador)

print(f"Você jogou: {jogada_jogador}")
print(f"O computador jogou: {jogada_computador}")
print(f"Resultado: {resultado}")


