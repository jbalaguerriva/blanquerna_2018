def main():

    # Una lista es un conjunto de valores dispuestos en secuencia

    squares = [1, 4, 9, 16]
    sum = 0

    for num in squares:
        # Operador nuevo ==> sum = sum + num
        sum += num

    print(sum)

    # La funcion range(x) genera una lista de valores desde 0 a x-1

    for i in range(100):
        print(i)

    # Valores de 10 a 100

    for i in range(10,100):
        print (i)

    # De 10 a 100 en pasos de 10

    for i in range(10,100,10):
        print(i)

    # NO FUNCIONA...

    for i  in range(100,10):
        print(i)

    # De 100 a 10 en pasos de -10

    for i in range(100,10,-10):
        print(i)


main()
