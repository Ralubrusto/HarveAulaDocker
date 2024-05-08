import mysql.connector

def get_mysql_connector():
    conn = mysql.connector.connect(
        user='user_python', 
        password='pass',
        host='localhost',
        database='minhadatabase',
        port='3306'
    )
    return conn

def salva_resultado(nome_jogador, jogador, computador, resultado):
    conn = get_mysql_connector()
    if conn.is_connected():
        print("Conexão com o banco estabelecida com sucesso!")
    cursor = conn.cursor()

    query = f"""
        INSERT INTO tb_jogodavelha_resultados 
            (nome, jogada_jogador, jogada_computador, resultado) 
        VALUES  
            ('{nome_jogador}', '{jogador}', '{computador}', '{resultado}');
    """

    cursor.execute(query)
    conn.commit()
    cursor.close()
    print("Resultado salvo com sucesso!")