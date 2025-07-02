eleccion = int(input("1 o cualquiera"))
total = 0
if eleccion == 1:
  valor = True
else:
  valor = False
  
while valor == True:
  producto, cantidad, precio = input("pone el producto, cantidad y precio").split()
  total = total + float(cantidad) * float(precio)
  eleccion = int(input("1 o cualquiera"))
  if eleccion == 1:
    valor = True
  else:
    valor = False
print("el costo total es: ", total)