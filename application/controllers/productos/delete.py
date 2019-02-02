import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, codigo):
        productos = config.model_productos.select_producto(codigo)
        return config.render.delete(productos)

    def POST(self, codigo):
        formulario = web.input()
        codigo = formulario['codigo']
        config.model_productos.delete_producto(codigo)
        raise web.seeother('/productos')
