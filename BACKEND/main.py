## Rutas del proyecto

## Importacion del objeto
# Aplicacion
from fastapi import FastAPI

from controllers.categoria_controller import router as categoria_router
from controllers.chat_controller import router as chat_router
from controllers.detalle_pedido_controller import router as detalle_pedido_router
from controllers.inventario_controller import router as inventario_router
from controllers.item_controller import router as item_router
from controllers.notificacion_controller import router as notificacion_router
from controllers.pedido_controller import router as pedido_router
from controllers.producto_controller import router as producto_router
from controllers.resena_controller import router as resena_router
from controllers.rol_controller import router as rol_router
from controllers.usuario_controller import router as usuario_router
from controllers.video_controller import router as video_router

## Crear el objeto aplicacion
app = FastAPI()

app.include_router(categoria_router)
app.include_router(producto_router)
app.include_router(usuario_router)
app.include_router(rol_router)
app.include_router(inventario_router)
app.include_router(item_router)
app.include_router(pedido_router)
app.include_router(chat_router)
app.include_router(detalle_pedido_router)
app.include_router(notificacion_router)
app.include_router(resena_router)
app.include_router(video_router)
