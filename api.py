from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from models import TalleristaModel
from typing import List
from utils.openai_api import description_filter
from utils.google_api import google_custom_search
from utils.jumbo_webscrap import search_supply

app = FastAPI()
client = AsyncIOMotorClient('mongodb://localhost:27017')
db = client['Proyecto']


@app.post('/talleristas/', response_model=List[TalleristaModel])
async def save_talleristas(talleristas: List[TalleristaModel]):
    if not talleristas:
        raise HTTPException(
            status_code=400, detail="No se proporcionaron talleristas para guardar.")
    for tallerista in talleristas:
        existing_tallerista = await db['Talleristas'].find_one(tallerista.dict())
        if existing_tallerista:
            raise HTTPException(
                status_code=409, detail="El tallerista ya existe en la base de datos.")
    result = await db['Talleristas'].insert_many([tallerista.dict() for tallerista in talleristas])
    return talleristas


@app.get('/talleristas/', response_model=List[TalleristaModel])
async def get_talleristas():
    talleristas = await db['Talleristas'].find().to_list(128)
    return talleristas


@app.delete('/talleristas/', response_model=dict)
async def delete_talleristas(linkedins: List[str]):
    if not linkedins:
        raise HTTPException(
            status_code=400, detail="No se proporcionaron linkedins para borrar.")
    result = await db['Talleristas'].delete_many({"linkedin": {"$in": linkedins}})
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404, detail="No se encontraron talleristas con los linkedins proporcionados.")
    return {"mensaje": f"{result.deleted_count} documentos eliminados exitosamente."}


@app.get('/filtrar/', response_model=str)
async def filtrar_descripcion(prompt: str):
    if not prompt:
        raise HTTPException(
            status_code=400, detail="No se proporcionó un prompt para filtrar.")
    return description_filter(prompt)


@app.get('/buscar/talleristas/', response_model=List[dict])
async def buscar_talleristas(prompt: str):
    if not prompt:
        raise HTTPException(
            status_code=400, detail="No se proporcionó un prompt para buscar.")
    return google_custom_search(prompt)


@app.get('/buscar/insumos/', response_model=List[dict])
async def buscar_insumos(prompt: str):
    if not prompt:
        raise HTTPException(
            status_code=400, detail="No se proporcionó un prompt para buscar.")
    return search_supply(prompt)
