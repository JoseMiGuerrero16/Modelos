from pydantic import BaseModel

class TalleristaModel(BaseModel):
    nombre: str
    linkedin: str
    foto_perfil: str

class InsumoModel(BaseModel):
    # Definir aquí las propiedades del insumo
    pass

class HistorialModel(BaseModel):
    # Definir aquí las propiedades del historial de talleres
    pass

class TallerlModel(BaseModel):
    # Definir aquí las propiedades del historial de talleres
    pass
