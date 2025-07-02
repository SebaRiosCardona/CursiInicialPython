eleccion = int(input("1 o cualquiera"))
compra = {}
total = 0
if eleccion == 1:
  valor = True
else:
  valor = False
  
while valor == True:
  producto, cantidad, precio = input("pone el producto, cantidad y precio").split()
  total = total + float(cantidad) * float(precio)
  compra.append([producto, cantidad, precio])
  eleccion = int(input("1 o cualquiera"))
  if eleccion == 1:
    valor = True
  else:
    valor = False
print("el costo total es: ", total)
print(compra)