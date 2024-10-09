from sqlalchemy import create_engine,event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine


#datos para la conexion a BD

dataBaseName="gestordb"

#Usuario BD
userName="root"

#Contraseña del usuario
userPassword=""

#PUERTO DE CONEXION
connectionPort=3306

#SERVIDOR CONEXION
server="localhost"

#creando la conexion
dataBaseConnection=f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"

#creo el motor de conexion
engine=create_engine(dataBaseConnection)

#abrir la sesion con la bd
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

