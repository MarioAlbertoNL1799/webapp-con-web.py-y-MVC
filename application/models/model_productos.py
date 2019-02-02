import config as config

db = config.db

'''
Seleccion de registros de productos
'''
def select_productos():
    try:
        return db.select('productos')
    except Exception as e:
        print "Model select_productos Error {}".format(e.args)
        print "Model select_productos Message {}".format(e.message)
        return None

'''
Seleccion de un registro con coincidencia
'''
def select_producto(codigo):
    try:
        return db.select('productos',where='codigo=$codigo', vars=locals())[0]
    except Exception as e:
        print "Model select_producto Error {}".format(e.args)
        print "Model select_producto Message {}".format(e.message)
        return None

'''
Ingreso de nuevo producto
'''
def insert_producto(nombre,marca,categoria,precio):
    try:
        return db.insert('productos', nombre=nombre,marca=marca,categoria=categoria,precio=precio)
    except Exception as e:
        print "Model insert_producto Error {}".format(e.args)
        print "Model insert_producto Message {}".format(e.message)
        return None

'''
Eliminar producto
'''
def delete_producto(codigo):
    try:
        return db.delete('productos', where='codigo=$codigo',vars=locals())
    except Exception as e:
        print "Model delete_producto Error {}".format(e.args)
        print "Model delete_producto Message {}".format(e.message)
        return None

'''
Actualizar datos
'''
def update_producto(codigo ,nombre, marca, categoria, precio):
    try:
        return db.update('productos',
                         nombre=nombre,
                         marca=marca,
                         categoria=categoria,
                         precio=precio,
                         where='codigo=$codigo', vars=locals())
    except Exception as e:
        print "Model update_producto Error {}".format(e.args)
        print "Model update_producto Error {}".format(e.args)
        return None
