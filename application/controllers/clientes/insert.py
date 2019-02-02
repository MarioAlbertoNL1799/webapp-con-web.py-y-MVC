import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):
        return config.render.insert()

    def POST(self):
        formulario = web.input()
        nombre = formulario['nombre']
        apellidos = formulario['apellidos']
        correo = formulario['correo']
        telefono = formulario['telefono']
        config.model_clientes.insert_cliente(nombre,apellidos, correo,telefono)
        raise web.seeother('/clientes')
