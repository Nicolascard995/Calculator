# Definir función de suma
def sumar(num1, num2):
  return num1 + num2

# Definir función de resta
def restar(num1, num2):
  return num1 - num2

# Definir función de multiplicación
def multiplicar(num1, num2):
  return num1 * num2

# Definir función de división
def dividir(num1, num2):
  # Manejar el caso donde el segundo número es cero
  if num2 == 0:
    print("¡Error! No se puede dividir por cero.")
    return None
  return num1 / num2
  
# Mostrar instrucciones
print('Seleccione una operación')
print('1. Sumar')
print('2. Restar')
print('3. Multiplicar')
print('4. Dividir')

# Tomar entrada del usuario 
opcion = input('Ingrese la operación que desea realizar (1/2/3/4): ')

# Tomar entrada de números y manejar el caso donde no se ingresó un número válido
try:
  num1 = float(input('Ingrese el primer número: '))
  num2 = float(input('Ingrese el segundo número: '))
except ValueError:
  print("¡Error! Debe ingresar un número válido.")
  exit()

# Evaluar la opcion ingresada por el usuario y llamar a la funcion correspondiente
if opcion == '1':
  print(num1, '+', num2, '=', sumar(num1, num2))
elif opcion == '2':
  print(num1, '-', num2, '=', restar(num1,num2))
elif opcion == '3':
  print(num1, '*', num2, '=', multiplicar(num1, num2))
elif opcion == '4':
  resultado = dividir(num1, num2)
  if resultado is not None:
    print(num1, '/', num2, '=', resultado)
else:
  print('Opción inválida')
