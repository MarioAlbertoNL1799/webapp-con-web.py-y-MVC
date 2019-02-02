import web
import config as config

class Update:
    def __init__(self):
        pass
    def GET(self, codigo):
        producto = config.model_productos.select_producto(codigo)
        return config.render.update(producto)

    def POST(self,codigo):
        formulario = web.input()
        nombre = formulario['nombre']
        marca = formulario['marca']
        categoria = formulario['categoria']
        precio = formulario['precio']
        config.model_productos.update_producto(codigo,nombre,marca,categoria,precio)
        raise web.seeother('/productos')
