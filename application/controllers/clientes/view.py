import web
import config as config

class View:
    def __init__(self):
        pass

    def GET(self,id):
        cliente = config.model_clientes.select_nombre(id)
        return config.render.view(cliente)
