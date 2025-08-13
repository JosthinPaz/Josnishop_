# JOSNISHOP - Proyecto Full Stack 

Este proyecto es una tienda en línea desarrollada con React (frontend) y FastAPI (backend). 

Incluye instrucciones básicas de uso y configuración de dependencias iniciales. 

 

## 📁 Estructura del Proyecto 

JOSNISHOP/ 
├── BACKEND/    # API y lógica de negocio (Python, FastAPI) 
├── frontend/   # Interfaz de usuario (React, JavaScript/TypeScript) 
  

 

## 🚀 Instrucciones Básicas de Uso 

#### 1. Clonar el repositorio 

git clone <URL-del-repositorio> 
cd JOSNISHOP 
  

#### 2. Configurar el Backend 

cd BACKEND 
 

Instala las dependencias:pip install -r requirements.txt 
  

Ejecuta el servidor:uvicorn main:app --reload 
  

Accede a la API en http://localhost:8000 

 

#### 3. Configurar el Frontend 

cd frontend 
  

Instala las dependencias:npm install 
  

Inicia la aplicación React:npm start 
  

Accede a la web en http://localhost:3000 

 

## ⚙️ Dependencias Iniciales 

Backend (BACKEND/requirements.txt) 

fastapi 

sqlalchemy 

alembic 

pydantic 

black 

isort 

ruff 

y otras necesarias para la API 

Frontend (frontend/package.json) 

react 

react-dom 

react-scripts 

react-router-dom 

typescript 

@types/react 

@types/react-dom 

@testing-library/react 

@testing-library/jest-dom 

 

## 📝 Notas 

El backend y el frontend funcionan de manera independiente. 

Puedes modificar la configuración de la base de datos en BACKEND/db/database.py. 

Para agregar nuevas dependencias, usa pip install <paquete> en backend y npm install <paquete> en frontend. 

Consulta la documentación interna de cada carpeta para detalles específicos. 

 

👤 Autores 

Josthin Paz y Nicol Amaya 
