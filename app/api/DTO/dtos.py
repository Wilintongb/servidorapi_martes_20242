from pydantic import BaseModel, Field
from datetime import date

#LOS DTO SON CLASES QUE ESTABLECEN EL MODELO DE TRANSFERENCIA DE DATOS
class UsuarioDTOPeticion(BaseModel):
    nombres:str
    fechaNacimiento:date
    ubicacion:str
    metaAhorro:float
    class Config:
        orm_mode=True #ORM es el traductor entre python y la BD

class UsuarioDTORespuesta(BaseModel):
    id:int
    nombres:str
    metaAhorro:float
    class Config:
        orm_mode=True #ORM es el traductor entre python y la BD

class GastoDTOPeticion(BaseModel):
    descripcion:str
    valor:int
    fecha:date
    class Config:
        orm_mode=True

class GastoDTORespuesta(BaseModel):
    id:int
    descripcion:str
    valor:int
    fecha:date
    class Config:
        orm_mode=True

class CategoriaDTOPeticion(BaseModel):
    nombre:str
    descripcion:str
    fotoCategoria:str
    class Config:
        orm_mode=True

class CategoriaDTORespuesta(BaseModel):
    id:int
    nombre:str
    descripcion:str
    fotoCategoria:str
    class Config:
        orm_mode=True

class IngreseDTOPeticion(BaseModel):
    valor:int
    descripcion:str
    fecha:date
    class Config:
        orm_mode=True

class IngresoDTORespuesta(BaseModel):
    id:int
    valor:int
    descripcion:str
    fecha:date
    class Config:
        orm_mode=True
    
