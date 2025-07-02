el_id = 0
compra = []
total = 0

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

def alta(producto, cantidad, precio):
  global total
  global el_id
  
  total = total + float(cantidad) * float(precio)
  compra[el_id] = {'producto':producto, 'cantidad': cantidad, 'precio': precio}
  el_id += 1
  print("estoy en alta")

def borrar(id_borrar):
  global total
  global compra
  print(compra[id_borrar])
  
  total = total - (float(compra[id_borrar]['cantidad']) * float(compra[id_borrar]['precio']))
  del compra[id_borrar]
  print("estoy en alta")

def listar():
  global compra
  global total
  print(compra)
  print(total)
  print("estoy en listar")

def modificar(id_modificar, precio):
  global compra
  global total
  antes = float(compra[id_modificar]['cantidad'])*float(compra[id_modificar]['precio'])
  compra[id_modificar]['precio'] = precio 
  despues = float(compra[id_modificar]['cantidad'])*float(compra[id_modificar]['precio'])
  
while valor == True:
  print("eleccion: ", eleccion)
  
  if eleccion == "a":
    producto, cantidad, precio = input("ingrese el nombre, cantidad y precio").split()
    alta(producto, cantidad, precio)
  if eleccion == "e":
    id_borrar = input("ingrese el id del elemento a borrar: ")
    borrar(int(id_borrar))
  if eleccion == "l":
    listar()
  if eleccion == "m":
    id_modificar, precio = input("ingrese el id y el nuevo precio").split()
    modificar(int(id_modificar, float(precio)))
  else:
    break
  
menu()

