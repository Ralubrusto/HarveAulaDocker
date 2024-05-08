CREATE DATABASE minhadatabase;
USE minhadatabase;

CREATE TABLE tb_jogodavelha_resultados (
    nome               VARCHAR(255),
    jogada_jogador     VARCHAR(255),
    jogada_computador  VARCHAR(255),
    resultado          VARCHAR(255),
    dt_atualizacao     TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);
