from sqlalchemy import create_engine

# connection string
# represenat la base de datos a conectar
# dependiendo la base de datos que se use y el lenguaje de programación
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:admin@localhost:3315/josnishop"

# crea el objeto de conexion(permite conectarse a la base de datos)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
