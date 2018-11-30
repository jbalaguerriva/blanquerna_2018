def main():

    # Inicializacion y operaciones sobre cadenas

    # Asignacion de una cadena

    tString = "Hola mundo"

    # Segundo caracter de la cadena (ojo, empieza en 0)

    print(tString[1])

    # Longitud de una cadena

    print(len(tString))

    # Concatenacion de dos cadenas

    print(tString + " otra vez...")

    # Conversion de un flotante a cadena

    e = 2.71
    print("El numero e es: " + str(e))

    # Conversiones a mayuscula/minuscula

    print(tString.lower())
    print(tString.upper())

    # Parto la cadena por espacios, y la vuelvo a unir

    tokens = tString.split(" ")
    print(tokens)
    nuevaString = (" ").join(tokens)

    print("La cadena nueva es " + nuevaString)

    # Secuencias de control

    tString = tString + "\n\n\n"

    print(tString)

    # 'Rodajas de cadenas ('slices'), ojo, el indice empieza en cero

    rString = "Rodaja"

    print(rString[2:4])
    print(rString[1:])
    print(rString[4])
    print(rString[-2])
    print(rString[0:-1])
    print(rString[-4:])

    # Impresion de multiples variables en una sola cadena

    # Usando la notacion % : %f es flotante, %d es entero, %s es cadena


    pString = "El numero e es: %f y la cadena es %s y el numero es %d" % (e,rString, 10)

    print(pString)

main()