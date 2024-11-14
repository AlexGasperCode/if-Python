#Ejercicio 1
numero = int(input("Ingrese un número: "))
if numero > 5:
    print("En número es mayor a 5")
else:
    print("El número es menor a 5")

#Ejercicio 2
a = 47
b = 20
if a > b:
    print(a,"es mayor",b)
else:
    print(b,"es mayor",a)

#Ejercicio 3
edad = int(input("Ingresa tu edad: "))
if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad <= 50:
    print("Eres mayor de edad")

#Ejercicio 4
num1 = int(input("Ingrese el número: "))
if num1 == 10:
    print("El numero es igual")
    if num1 <= 10:
        print("El numero es menor")
    if num1 > 10:
        print("El numero es mayor")
else:
    print("El número es: " ,num1)

#Ejercicio 5
entrada = int(input("Ingrese la nota: "))
nota = int(entrada)
if nota >= 5:
    print("Aprueba el semestre")
elif nota <= 5:
    print("Reprueba el semestre")
else:
    print("Esta en recuperación")
