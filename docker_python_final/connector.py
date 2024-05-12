import mysql.connector

def get_mysql_connector():
    conn = mysql.connector.connect(
        user='SEU_USUARIO',  # EDITE AQUI!! Coloque o usuário que você criou
        password='pass',     # E aqui, a senha para ele
        host='localhost',
        database='minhadatabase',  # Só altere caso tenha mudado o nome da tabela
        port='3306'
    )
    return conn

def salva_resultado(nome_jogador, jogador, computador, resultado):
    conn = get_mysql_connector()
    if conn.is_connected():
        print("Conexão com o banco estabelecida com sucesso!")
    cursor = conn.cursor()


    # É necessário alterar essa query abaixo apenas se você mudou o nome da tabela
    query = f"""
        INSERT INTO tb_pedrapapeltesoura_resultados 
            (nome, jogada_jogador, jogada_computador, resultado) 
        VALUES  
            ('{nome_jogador}', '{jogador}', '{computador}', '{resultado}');
    """

    cursor.execute(query)
    conn.commit()
    cursor.close()
    print("Resultado salvo com sucesso!")