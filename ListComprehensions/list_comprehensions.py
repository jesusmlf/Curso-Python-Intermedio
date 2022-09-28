from os import sched_getscheduler


def run():
    #Crear una lista con los primeros 100 numeros naturales elevados al cuadrado.
    squares = []
    for i in range(1,101):
        squares.append(i**2)
    
    #Crear una lista con los primeros 100 numeros naturales elevados al cuadrado que no sean divisibles entre 3.
    squares_not_divisible_by_3 = []
    for i in range(1,101):
        if i%3 != 0:
            squares_not_divisible_by_3.append(i**2)
    

    #Ahora resolveremos los mismos problemas utilizando list comprehensions:
    #Crear una lista con los primeros 100 numeros naturales elevados al cuadrado.
    squares = [i**2 for i in range(1,101)]
    print(squares)
    #Crear una lista con los primeros 100 numeros naturales elevados al cuadrado que no sean divisibles entre 3.
    squares_not_divisible_by_3 = [i**2 for i in range(0,101) if i%3 != 0]
    print(squares_not_divisible_by_3)

    """
    Reto: Crear, con un list comprehensions, una lista de todos los múltiplos de 4 que a la vez también son múltiplos
    de 6 y de 9, hasta 5 digitos.
    """
    nums = [i for i in range(1,10000) if i%36 == 0]
    print(nums)
    
if __name__ == '__main__':
    run()