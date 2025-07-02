compra = []
total = 0

# ########################################
# VISTA
# lo denominamos como vista ya que va a ser lo que va a interactuar con el usuario. (esto tranquilamente podria ser una
# interfaz grafica GUI). La vista no tiene logica ni toma decision
#
# NO SE SUELE TENER LA VISTA, MODELO, Y CONTROLADOR EN EL MISMO ARCHIVO, SINO QUE SE LOS PONE EN OTRO ARCHIVO Y SE LOS IMPORTA ACA (de
# esta forma vamos a saber que el problema esta en la vista si tenemos un problema en la interaccion con el usuario)
# ########################################

def menu ():
  print("\n Eleji una oprcion:")
  print("(a) agregar un producto")
  print("(b) eliminar un producto")
  print("(c) listar producto")
  print("(d) modificar un producto")
  print("o cualquier tecla para salir")
  global valor
  global eleccion
  eleccion = input()
  if eleccion == "a" or eleccion == "e" or eleccion == "l" or eleccion == "m":
    valor = True
    print("ingresada")
  else:
    valor = False
    print("chau")

menu()

# ########################################
# MODELO
# es el modelo porque aca se define que accion corresponde a la que va a ejecutar el controlador, es decir decidimos que va a suceder
# cuando se ejecute la funcion alta()
#
# NO SE SUELE TENER LA VISTA, MODELO, Y CONTROLADOR EN EL MISMO ARCHIVO, SINO QUE SE LOS PONE EN OTRO ARCHIVO Y SE LOS IMPORTA ACA (
# entonces si el problema esta en la alta de los datos, sabemos que el problema esta en el modelo ya que se esta ejecutando mal la funcion)
# ########################################
def alta(): print("estoy en alta")
def borrar(): print("estoy en borrar")
def listar(): print("estoy en listar")
def modificar(): print("estoy en modificar")


# ########################################
# CONTROLADOR
# el controlador es el que va a decidir que hacer con la informacion que nos envie el usuario a traves de la vista, en este caso con
# un condicional while, entonces el controlador decide, en base a lo que cargo el usuario si hace la alta, la baja, etc. o vuelve al
# menu para volverle a preguntar al usuario o salir del programa
#
# (y si el problema esta en el flujo de la informacion vamos a revisar el controlador)
# ########################################

while valor == True:
  print("eleccion: ", eleccion)
  
  if eleccion == "a":
    alta()
  if eleccion == "e":
    borrar()
  if eleccion == "l":
    listar()
  if eleccion == "m":
    modificar()
  
  menu()