CREATE DATABASE minhadatabase;  -- Se quiser mude o nome da database, mas lembre de alterar nos outros lugares também
USE minhadatabase;

CREATE TABLE tb_jogodavelha_resultados (  -- Se quiser mude o nome da tabela
    -- coluna para o nome,
    -- coluna para a jogada do jogador,
    -- coluna para a jogada do computador,
    -- coluna para o resultado,
    dt_atualizacao     TIMESTAMP DEFAULT CURRENT_TIMESTAMP()  -- não se preocupe com esta coluna
);
