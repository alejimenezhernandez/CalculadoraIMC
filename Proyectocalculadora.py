# Proyecto Calculadora IMC

print("                                                                 Bienvenido !!\n")  # Mensaje de Bienvenida al usuario
print("                                               Ingresaste a la calculadora de Indice de masa corporal (IMC)\n")  # Indica el nombre de proyecto
print("A continuación ingresa los datos solicitados\n")  # Se indica al usuario que se le pedirá información la cual debe ingresar

personas = int(input("personas: \n\n"))  # Se solicita ingrese personas a realizar el ejercicio

while personas > 0:  # Se establece que mientras sea mayor que cero se repita el bucle de lo contrario se finaliza

    nombre = input("\n  ¿Cuál es tu nombre? \n\n  ")  # Solicitar el nombre al usuario
    nombre1 = input("\n  ¿Cuál es tu apellido paterno? \n\n  ")  # Solicitar apellido paterno
    nombre2 = input("\n  ¿Cuál es tu apellido materno? \n\n  ")  # Solicitar apellido materno

    print(f"\n   Hola {nombre} {nombre1} {nombre2}")  # Imprimir saludo y nombre completo ingresado

    edad = int(input("\n  ¿Cuántos años tienes?\n\n  "))  # Solicitar que ingrese su edad
    print(f"\n  Tienes {edad} años")  # Imprimir la edad ingresada

    peso = float(input("\n  ¿Cuál es tu peso en (Kg)?\n\n  "))  # Solicitar su peso en kilogramos
    print(f"\n  Tu peso actual es {peso} kg.")  # Imprimir el peso ingresado

    estatura = float(input("\n  ¿Cuánto mides en (m)?\n\n  "))  # Solicitar que ingrese su estatura en metros
    print(f"\n  Mides {estatura} m.")  # Imprimir la estatura ingresada

    IMC = round(peso / estatura**2, 2)  # Calcular el IMC y con la función round redondear a 2 decimales
    print(f"\n  Tu IMC es: {IMC}")  # Imprimir el resultado del IMC

    if IMC < 18.9: # Con el resultado obtenido determinar el rango del IMC e imprimir de acuerdo al rango que se encuentre
        print("\n  De acuerdo a tu IMC, tu peso actual es bajo")
    elif 18.50 <= IMC <= 24.99:
        print("\n  De acuerdo a tu IMC, tu peso actual es normal")
    elif 25.00 <= IMC <= 29.99:
        print("\n  De acuerdo a tu IMC, tienes sobrepeso")
    elif 30.00 <= IMC <= 34.99:
        print("\n  De acuerdo a tu IMC, tienes obesidad leve")
    elif 35.00 <= IMC <= 39.99:
        print("\n  De acuerdo a tu IMC, tienes obesidad media")
    elif IMC >= 40.00:
        print("\n  De acuerdo a tu IMC, tienes obesidad mórbida")

    personas -= 1  # Decrementar el contador de personas