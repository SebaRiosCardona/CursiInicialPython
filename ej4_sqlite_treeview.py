from tkinter import *
from tkinter.messagebox import *
import sqlite3 #Aca nos conectamos a una base de datos de tipo SQL llamado sqlite3 (lo usamos porque ya viene con python y no hay que instalar nada adicional
               #La bas de datos sqlite3 por defecto crea una columna llamada id en donde lo valores son autoincrementales, es decir que no lo teng que generar yo,
               #sino que la base de datos ya lo genera
from tkinter import ttk
import re
# ##############################################
# MODELO
# ##############################################

#en esta primer parte lo que hacemos es crear la estructura de la base de de datos con la cual nos vamos a conectar y vamos a
# ejecutar las funciones alta, baja, modificacion y consulta
def conexion():
    con = sqlite3.connect("mibase.db") #aca tenemos una funcion en donde se crea la base de datos, y si ya existe no se crea
                                       #pero abre la conexion con es bd
    return con
	
def crear_tabla():
    con = conexion()
    cursor = con.cursor()
	    
    #esta tabla se va a encontrar en la base de datos
    sql = """CREATE TABLE productos #la tabla se va a llamar "producto", y la cual va a tener las siguiente 4 columnas
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             producto varchar(20) NOT NULL,
             cantidad real,
             precio real)
    """
    cursor.execute(sql)
    con.commit()
	
#aca voy a intentar atrapar al error, en caso que el "try" no se ejecute bien el programa no se va a detener, sino que va a imprimir lo que sale por el "except"
try:
    conexion() #aca voy a llamar a la funcion conexion
    crear_tabla() #aca voy a llamar a la funcion crear_producto
except:
    print("Hay un error")

#
def alta(producto, cantidad, precio, tree):
 
    print(producto, cantidad, precio)
    
    #en los otros ejercicios de clases, la diferencia es que abriamos la lista/diccionario, guardamos los datos en esa lista/diccionario y avisabamos que se realizo correctamente
    #es decir que antes, cuando usabamos un diccionario para guardar la informacion el codigo quedaba asi:
    #compra[el_id] = {'producto': producto, 'cantidad': cantidad, 'precio': precio}
    #el_id += 1
    #print("estoy en alta")
    con=conexion()
    cursor=con.cursor()
    data=(producto.get(), cantidad, precio)
    sql="INSERT INTO productos(producto, cantidad, precio) VALUES(?, ?, ?)"
    cursor.execute(sql, data)
    con.commit()
    producto.set("---")#con esto, cuando hago un alta, en la interfaz se va a ver "---"
    
    print("Estoy en alta todo ok")
    actualizar_treeview(tree) #con a la informacion no la voy a mostrar en consola, sino que voy a usar una interfaz grafica, voy a usar un tree view, pero
                              #la logica es la misma.
                              #cuando trabajamos con una interfaz a la informaicon no la tomamos con un "input", sino que usamos un "entry"

def borrar(tree):
    valor = tree.selection()
    print(valor)   #('I005',)
    item = tree.item(valor)
    print(item)    #{'text': 5, 'image': '', 'values': ['daSDasd', '13.0', '2.0'], 'open': 0, 'tags': ''}
    print(item['text'])
    mi_id = item['text']

    con=conexion()
    cursor=con.cursor()
    #mi_id = int(mi_id)
    data = (mi_id,)
    sql = "DELETE FROM productos WHERE id = ?;" #aca nos comunicamos con una base de datos
    cursor.execute(sql, data)
    con.commit()
    tree.delete(valor)

def actualizar_treeview(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    sql = "SELECT * FROM productos ORDER BY id ASC"
    con=conexion()
    cursor=con.cursor()
    datos=cursor.execute(sql)

    resultado = datos.fetchall()
    for fila in resultado:
        print(fila)
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))

# ##############################################
# VISTA
# ##############################################
root = Tk()
root.title("Tarea POO")
        
titulo = Label(root, text="Ingrese sus datos", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

producto = Label(root, text="Producto")
producto.grid(row=1, column=0, sticky=W)
cantidad=Label(root, text="Cantidad")
cantidad.grid(row=2, column=0, sticky=W)
precio=Label(root, text="Precio")
precio.grid(row=3, column=0, sticky=W)

# Defino variables para tomar valores de campos de entrada
a_val, b_val, c_val = StringVar(), DoubleVar(), DoubleVar() # aca le pasamos que tipo de informacion va a guarda.
                                                            #StringVar() es una variable de tkinter, no de python, y esto es como una caja dentro de la cual puede ir
                                                            #texto. Para obtener ese texto y sacarlo de ahi tengo que hacer un .get() sobre ese StringVar()
w_ancho = 20

#con el Entry se envian los parametros a la aplicacion, la forma correcta de hacerlo es definiendo la entrada correcta de texto y asociando una variable (ej: a_val
# va con entrada1, b_val va con entrada2 y asi)
entrada1 = Entry(root, textvariable = a_val, width = w_ancho) 
entrada1.grid(row = 1, column = 1)
entrada2 = Entry(root, textvariable = b_val, width = w_ancho) 
entrada2.grid(row = 2, column = 1)
entrada3 = Entry(root, textvariable = c_val, width = w_ancho) 
entrada3.grid(row = 3, column = 1)
# --------------------------------------------------
# TREEVIEW
# --------------------------------------------------
tree = ttk.Treeview(root)
tree["columns"]=("col1", "col2", "col3")
tree.column("#0", width=90, minwidth=50, anchor=W)
tree.column("col1", width=200, minwidth=80)
tree.column("col2", width=200, minwidth=80)
tree.column("col3", width=200, minwidth=80)
tree.heading("#0", text="ID")
tree.heading("col1", text="Producto")
tree.heading("col2", text="cantidad")
tree.heading("col3", text="precio")
tree.grid(row=10, column=0, columnspan=4)

#para pasar parametros, la informacion se manda mediante una funcion lambda, 
boton_alta=Button(root, text="Alta", command=lambda:alta(a_val.get(), b_val.get(), c_val.get(), tree)) #aca estoy haciendo el .get() de a_val, es decir de cada StringVar()
#si quisiera enviar un dato para modificar el contenido de esa caja "StringVar()" tengo que hacerlo con un .set()
boton_alta.grid(row=6, column=1)

boton_borrar=Button(root, text="Borrar", command=lambda:borrar(tree))
boton_borrar.grid(row=8, column=1)
root.mainloop()