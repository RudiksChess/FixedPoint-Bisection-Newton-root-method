"""
@author: Rudik Roberto Rompich
@carnet: 19857
@clase: Herramientas Tecnologicas
"""
import numpy as np

f1 = lambda x: x - np.cos(x)
f2 = lambda x: x ** 2 - 2
f3 = lambda x: np.log(x) + x
f4 = lambda x: np.exp(np.sin(x)) + x - 2

f1d = lambda x: 1 + np.sin(x)
f2d = lambda x: 2 * x
f3d = lambda x: (1 / x) + 1
f4d = lambda x: np.cos(x) * np.exp(np.sin(x)) + 1


def biseccion(funcion, min, max, iteraciones, decimales):
    for i in range(1, iteraciones + 1):
        resultado = (min + max) / 2
        if funcion(min) * funcion(resultado) < 0:
            min = min
            max = resultado
        elif funcion(max) * funcion(resultado) < 0:
            min = resultado
            max = max

    print("\nMétodo de bisección\n" +
          "La solución de la ecuación es aproximadamente: " + str(round(resultado, decimales)) +
          "\nEl número de iteraciones fue: " + str(iteraciones) + "\n")


def puntoFijo(funcion, aprox, iteraciones, decimales):
    tolerancia = 10 ** -4
    for i in range(0, iteraciones):
        val = funcion(aprox)
        if abs(val - aprox) < tolerancia:
            return ("\nMétodo de punto fijo\n" +
                    "La solución de la ecuación es aproximadamente: " + str(round(val, decimales)) +
                    "\nEl número de iteraciones fue: " + str(iteraciones) + "\n")

        aprox = val
    return "\nEl metodo de punto fijo falla después de " + str(
        iteraciones) + " iteraciones. Intentar de nuevo con otra aproximación"


def newtonRaphson(funcion, derivada, aprox, iteraciones, decimales):
    tolerancia = 10 ** -4
    for i in range(0, iteraciones):
        val = aprox - (funcion(aprox) / derivada(aprox))
        if abs(val - aprox) < tolerancia:
            return ("\nMétodo de Newton - Raphson\n" +
                    "La solución de la ecuación es aproximadamente: " + str(round(val, decimales)) +
                    "\nEl número de iteraciones fue: " + str(iteraciones) + "\n")
        aprox = val
    return "\nEl metodo de Newton-Raphson falla después de " + str(
        iteraciones) + " iteraciones. Intentar de nuevo con otra aproximación"


lol = int(input("\n|BIENVENIDO A LA CALCULADORA DE SOLUCIONES APROXIMADAS | \n" +

                "SELECCIONE UNA FUNCIÓN PARA CALCULAR: \n\n" +
                "1. x- cox(x) = 0 \n" +
                "2. x^2 + 2 = 4 \n" +
                "3. ln(x) + x = 0 \n" +
                "4. e^(sin(x)) + x = 2 \n" +
                "5. Salir\n\n" +
                "OPCIÓN:"))

while lol != 5:

    try:

        if lol == 1:

            w = int(input("¿En dónde comienza el intervalo?: "))
            x = int(input("¿En dónde termina el intervalo?: "))
            y = int(input("Asignar una aproximación: "))
            z = int(input("Número máximo de iteraciones:"))
            v = int(input("Número de decimales del resultado:"))

            if f1(w) * f1(x) >= 0:
                print("\nEs un intervalo inválido para el método de bisección\n")
            else:
                biseccion(f1, w, x, z, v)

            print(puntoFijo(f1, y, z, v))

            print(newtonRaphson(f1, f1d, y, z, v))



        elif lol == 2:
            w = int(input("¿En dónde comienza el intervalo?: "))
            x = int(input("¿En dónde termina el intervalo?: "))
            y = int(input("Asignar una aproximación: "))
            z = int(input("Número máximo de iteraciones:"))
            v = int(input("Número de dígitos de exactitud del resultado:"))

            if f2(w) * f2(x) >= 0:
                print("\nEs un intervalo inválido para el método de bisección\n")
            else:
                biseccion(f2, w, x, z, v)

            print(puntoFijo(f2, y, z, v))

            print(newtonRaphson(f2, f2d, y, z, v))




        elif lol == 3:
            w = int(input("¿En dónde comienza el intervalo?: "))
            x = int(input("¿En dónde termina el intervalo?: "))
            y = int(input("Asignar una aproximación: "))
            z = int(input("Número máximo de iteraciones:"))
            v = int(input("Número de dígitos de exactitud del resultado:"))

            if f3(w) * f3(x) >= 0:
                print("\nEs un intervalo inválido para el método de bisección\n")
            else:
                biseccion(f3, w, x, z, v)

            print(puntoFijo(f3, y, z, v))

            print(newtonRaphson(f3, f3d, y, z, v))


        elif lol == 4:
            w = int(input("¿En dónde comienza el intervalo?: "))
            x = int(input("¿En dónde termina el intervalo?: "))
            y = int(input("Asignar una aproximación: "))
            z = int(input("Número máximo de iteraciones:"))
            v = int(input("Número de dígitos de exactitud del resultado:"))

            if f4(w) * f4(x) >= 0:
                print("\nEs un intervalo inválido para el método de bisección\n")
            else:
                biseccion(f4, w, x, z, v)

            print(puntoFijo(f4, y, z, v))

            print(newtonRaphson(f4, f4d, y, z, v))




        else:

            print("Vuelva a ingresar un valor válido")

        lol = int(input("\n|BIENVENIDO A LA CALCULADORA DE SOLUCIONES APROXIMADAS | \n" +

                        "SELECCIONE UNA FUNCIÓN PARA CALCULAR: \n\n" +
                        "1. x- cox(x) = 0 \n" +
                        "2. x^2 + 2 = 4 \n" +
                        "3. ln(x) + x = 0 \n" +
                        "4. e^(sin(x)) + x = 2 \n" +
                        "5. Salir\n\n" +
                        "OPCIÓN:"))


    except ValueError:

        print("ERROR: Está ingresando un valor no númerico")
