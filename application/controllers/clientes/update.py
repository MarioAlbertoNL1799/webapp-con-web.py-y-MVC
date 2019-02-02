import web
import config as config

class Update:
    def __init__(self):
        pass
    def GET(self, id):
        cliente = config.model_clientes.select_nombre(id)
        return config.render.update(cliente)

    def POST(self, id):
        formulario = web.input()
        nombre = formulario['nombre']
        apellidos = formulario['apellidos']
        correo = formulario['correo']
        telefono = formulario['telefono']
        config.model_clientes.update_cliente(id,nombre,apellidos,correo,telefono)
        raise web.seeother('/clientes')
