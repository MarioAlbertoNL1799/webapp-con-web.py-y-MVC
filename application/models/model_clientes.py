import config as config

db = config.db

'''
Seleccion de registros de clientes
'''
def select_clientes():
    try:
        return db.select('clientes')
    except Exception as e:
        print "Model select_clientes Error {}".format(e.args)
        print "Model select_clientes Message {}".format(e.message)
        return None

'''
Seleccion de un registro con coincidencia
'''
def select_nombre(id):
    try:
        return db.select('clientes',where='id=$id', vars=locals())[0]
    except Exception as e:
        print "Model select_nombre Error {}".format(e.args)
        print "Model select_nombre Message {}".format(e.message)
        return None

'''
Ingreso de nuevo cliente
'''
def insert_cliente(nombre,apellidos,correo,telefono):
    try:
        return db.insert('clientes', nombre=nombre,apellidos=apellidos,correo=correo,telefono=telefono)
    except Exception as e:
        print "Model insert_cliente Error {}".format(e.args)
        print "Model insert_cliente Message {}".format(e.message)
        return None

'''
Eliminar cliente
'''
def delete_cliente(id):
    try:
        return db.delete('clientes', where='id=$id',vars=locals())
    except Exception as e:
        print "Model delete_cliente Error {}".format(e.args)
        print "Model delete_cliente Message {}".format(e.message)
        return None

'''
Actualizar datos
'''
def update_cliente(id,nombre, apellidos, correo, telefono):
    try:
        return db.update('clientes',
                         nombre=nombre,
                         apellidos=apellidos,
                         correo=correo,
                         telefono=telefono,
                         where='id=$id', vars=locals())
    except Exception as e:
        print "Model update_cliente Error {}".format(e.args)
        print "Model update_cliente Error {}".format(e.args)
        return None
