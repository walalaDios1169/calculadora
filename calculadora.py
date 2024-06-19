
#sumar valores
def suma(num1, num2):
  res = num1 + num2
  return res

#restar valores
def resta(num1, num2):
  res = num1 - num2
  return res

#multiplicar valores
def multiplicacion(num1, num2):
  res = num1 * num2
  return res
#dividir valores
def dividir(num1, num2):
  if num2 !=0:
    res= num1 / num2
    return res
  else:
    print("no se puede dividir por 0")

#MENU
#con el while true y el break arriba me funciono como lo hizo usted no me funciono por eso la modificacion  
while True:
  
  print("1. suma")
  print("2. resta")
  print("3.multiplicar")
  print("4.dividir")
  print("5.salir")
  
  op=int(input("ingrese una opcion: "))

  if op==5:
    print("hasta luego")
    break
  

  numero1 = int(input("ingrese el primer numero: "))
  numero2 = int(input("ingrese el segundo numero: "))

  if op==1:
    print("el resultado de la suma es: ",suma(numero1, numero2))

  elif op ==2:
    print("el resultado de la resta es: ",resta(numero1, numero2))

  elif op ==3:
    print("el resultado de la multiplicacion es: ",multiplicacion(numero1, numero2))

  elif op ==4:
    print("el resultado de la divicion es: ",dividir(numero1, numero2))

  
  else:
      print("ingrese un valor valido")