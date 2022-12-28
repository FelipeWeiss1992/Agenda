import psycopg2

print("Teste de conexão.")

try:
    conn = psycopg2.connect(
    host = "192.168.1.100",
    port ="5432",
    database = "postgres", 
    user="postgres", password = "123456")
    print("Conectado.")

except Exception:
    print("Você está sem conexâo.")

if conn is not None:
    
    print("Sua Conexão está estabilizada.")

    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE usuario (
                        id_usuario serial,
                        nome VARCHAR(50) NOT NULL,
                        data_nascimento DATE NOT NULL,
                        cpf VARCHAR(11) NOT NULL,
                        username VARCHAR(50) NOT NULL,
                        senha VARCHAR(256) NOT NULL,
                      PRIMARY KEY(id_usuario));""")

    print("Tabela USUARIO criada.")
    
    cursor.execute("""CREATE TABLE evento (
                        id_evento serial,
                        data_evento DATE NOT NULL,
                        titulo VARCHAR(50) NOT NULL,
                        descricao VARCHAR(200) NOT NULL,
                        publico BOOL NOT NULL,
                        fk_usuario INT NOT NULL,
                      PRIMARY KEY (id_evento),
                      FOREIGN KEY (fk_usuario)
                        REFERENCES usuario (id_usuario));""")
        
    print("Tabela EVENTO criada.")

    conn.commit()
    cursor.close()
    conn.close()