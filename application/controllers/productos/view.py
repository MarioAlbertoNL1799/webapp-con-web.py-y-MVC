import web
import config as config

class View:
    def __init__(self):
        pass

    def GET(self,codigo):
        producto = config.model_productos.select_producto(codigo)
        return config.render.view(producto)
