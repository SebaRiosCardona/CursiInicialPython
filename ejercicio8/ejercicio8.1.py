compra = []
total = 0

# ########################################
# VISTA
# lo denominamos como vista ya que va a ser lo que va a interactuar con el usuario. (esto tranquilamente podria ser una
# interfaz grafica GUI). La vista no tiene logica ni toma decision
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
# CONTROLADOR
# el controlador es el que va a decidir que hacer con la informacion que nos envie el usuario a traves de la vista, en este caso con
# un condicional while, entonces el controlador decide, en base a lo que cargo el usuario si hace la alta, la baja, etc. o vuelve al
# menu para volverle a preguntar al usuario o salir del programa
# ########################################

while valor == True:
  print("eleccion: ", eleccion)
  
  if eleccion == "a":
    print("aaaaaaaaaaaaa")
  if eleccion == "e":
    print("eeeeeeeeeeeee")
  if eleccion == "l":
    print("lllllllllllll")
  if eleccion == "m":
    print("mmmmmmmmmmmmm")
  else:
    break
  
  menu()
  