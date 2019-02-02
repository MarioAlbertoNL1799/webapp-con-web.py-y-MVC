import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, id):
        clientes = config.model_clientes.select_nombre(id)
        return config.render.delete(clientes)

    def POST(self, id):
        formulario = web.input()
        id = formulario['id']
        config.model_clientes.delete_cliente(id)
        raise web.seeother('/clientes')
