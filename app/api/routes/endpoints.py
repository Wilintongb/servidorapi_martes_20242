from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends

from app.api.DTO.dtos import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.DTO.dtos import GastoDTOPeticion, GastoDTORespuesta
from app.api.DTO.dtos import CategoriaDTOPeticion, CategoriaDTORespuesta
from app.api.DTO.dtos import IngreseDTOPeticion, IngresoDTORespuesta
from app.api.models.tablasSQL import Usuario
from app.api.models.tablasSQL import Gasto
from app.api.models.tablasSQL import Categoria
from app.api.models.tablasSQL import Ingreso
from app.database.configuration import SessionLocal, engine

rutas=APIRouter()

def conectarConBd():
    try:
        baseDatos=SessionLocal()
        yield baseDatos#yield es igual activar o producir

    except Exception as error:
        baseDatos.rollback()
        raise error

    finally:
        baseDatos.close()
        
#CONSTRUYENDO NUESTROS SERVICIOS

#Por definicion cada servicio (operacion o transaccion en BD) debe de programarse como una funcion
@rutas.post("/usuario", response_model=UsuarioDTORespuesta, summary="Registrar un usuario en la base de datos")
def guardarUsuario(datosUsuario:UsuarioDTOPeticion, database:Session=Depends(conectarConBd)):
    try:
        usuario=Usuario(
            nombres=datosUsuario.nombres,
            fechaNacimiento=datosUsuario.fechaNacimiento,
            ubicacion=datosUsuario.ubicacion,
            metaAhorro=datosUsuario.metaAhorro
        )
        #aca le ordenando a la BD 
        database.add(usuario)
        database.commit()
        database.refresh(usuario)
        return usuario

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}") #levantar o lanzar excepciones

@rutas.get("/usuario", response_model=List[UsuarioDTORespuesta], summary="Buscar todos los usuarios en la BD")    
def buscarUsuarios(database:Session=Depends(conectarConBd)):
    try:
        usuarios=database.query(Usuario).all()
        return usuarios

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se pueden buscar los usuarios {error}") #levantar o lanzar excepciones

@rutas.post("/gasto", response_model=GastoDTORespuesta, summary="Registrar un gasto en la base de datos")
def guardarGastos(datosGasto:GastoDTOPeticion, database:Session=Depends(conectarConBd)):
    try:
        gasto=Gasto(
            descripcion=datosGasto.descripcion,
            valor=datosGasto.valor,
            fecha=datosGasto.fecha
        )
        #aca le ordenando a la BD 
        database.add(gasto)
        database.commit()
        database.refresh(gasto)
        return gasto

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}") #levantar o lanzar excepciones

@rutas.get("/gasto", response_model=List[GastoDTORespuesta], summary="Buscar todos los gastos en la BD")    
def buscarGastos(database:Session=Depends(conectarConBd)):
    try:
        gastos=database.query(Gasto).all()
        return gastos

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se pueden buscar los gastos {error}") #levantar o lanzar excepciones

    
@rutas.post("/categoria", response_model=CategoriaDTORespuesta, summary="Registrar una categoria en la base de datos")
def guardarCategoria(datosCategoria:CategoriaDTOPeticion, database:Session=Depends(conectarConBd)):
    try:
        categoria=Categoria(
            nombre=datosCategoria.nombre,
            descripcion=datosCategoria.descripcion,
            fotoCategoria=datosCategoria.fotoCategoria
        )
        #aca le ordenando a la BD 
        database.add(categoria)
        database.commit()
        database.refresh(categoria)
        return categoria

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}") #levantar o lanzar excepciones

@rutas.get("/categoria", response_model=List[CategoriaDTORespuesta], summary="Buscar todas las categoria en la BD")    
def buscarCategoria(database:Session=Depends(conectarConBd)):
    try:
        categoria=database.query(Gasto).all()
        return categoria

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se pueden buscar las categoria {error}") #levantar o lanzar excepciones


@rutas.post("/ingreso", response_model=IngresoDTORespuesta, summary="Registrar un ingreso en la base de datos")
def guardarIngreso(datosIngreso:IngreseDTOPeticion, database:Session=Depends(conectarConBd)):
    try:
        ingreso=Ingreso(
            valor=datosIngreso.valor,
            descripcion=datosIngreso.descripcion,
            fecha=datosIngreso.fecha
        )
        #aca le ordenando a la BD 
        database.add(ingreso)
        database.commit()
        database.refresh(ingreso)
        return ingreso

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}") #levantar o lanzar excepciones

@rutas.get("/ingreso", response_model=List[IngresoDTORespuesta], summary="Buscar todos los ingresos en la BD")    
def buscarIngreso(database:Session=Depends(conectarConBd)):
    try:
        ingreso=database.query(Ingreso).all()
        return ingreso

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se pueden buscar los ingresos {error}") #levantar o lanzar excepciones


