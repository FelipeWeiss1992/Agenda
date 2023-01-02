SECRET_KEY = "agenda"

SQLALCHEMY_DATABASE_URI = \
    "{SGBD}://{usuario}:{senha}@{servidor}/{database}".format(
    SGBD = "postgresql",
    usuario = "postgres",
    senha = "123456",
    servidor = "192.168.1.100:5432",
    database = "postgres"
)