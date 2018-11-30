
def main():

    colors = ['rojo', 'azul', 'verde']
    print(colors[0])    ## rojo
    print(colors[2])    ## verde
    print(len(colors))  ## 3

    # OJO, la copia es por memoria (profunda, no superficial)

    colorsCopy = colors

    colorsCopy[0] = "amarillo"

    print(colors[0])
    print(colorsCopy[0])

    listaNombres = ['Pedro', 'Juan', 'Jose']

    # El operador 'in' comprueba si 'algo' es un elemento de una lista

    if 'Pedro' in listaNombres:
        print("Pedro esta en la lista")

    if 'Julio' in listaNombres:
        print("Julio esta en la lista")
    else:
        print("Julio NO esta en la lista")

    # Inicializo lista

    lista = ['Ana', 'Eva', 'Lola']

    # Anyado Laura al final, inserto Raquel en primera posicion

    lista.append('Laura')
    lista.insert(0, 'Raquel')

    # Agrego la lista 'Maria' y 'Luisa' a 'lista'



    lista.extend(['Maria', 'Luisa'])

    # La funcion repr hace de 'lista' algo imprimible
    print(lista)

    # Devuelve la posicion de 'Lola'
    print(lista.index('Lola'))

    # Elimina Lola y despues elimina el segundo elemento (indice 1)

    lista.remove('Lola')
    lista.pop(1)
    print(repr(lista))

    # Construir una lista desde cero

    listaNueva = []


    listaNueva.append("a")
    listaNueva.append("b")


    # Rodajas de listas

    listaRodajas = ['a','b','c','d',]


    # Imprime b y c

    print(listaRodajas[1:-1])

    # Sustituyo a y b por 'z'

    listaRodajas[0:2] = 'z'

    print(listaRodajas)


main()