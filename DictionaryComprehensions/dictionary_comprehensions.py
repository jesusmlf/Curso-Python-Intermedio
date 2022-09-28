def run():
    """
    Crear un diccionario cuyas llaves sean los 100 primeros numeros naturales y
    cuyos valores sean esos numeros elevados al cubo.
    """
    dictionary = {}
    for i in range(0,101):
        dictionary[i] = i**3
    #for key,value in dictionary.items():
    #    print(key,value)


    """
    Crear un diccionario cuyas llaves sean los 100 primeros numeros naturales
    no divisibles entre 3, y cuyos valores sean esos numeros elevados al cubo.
    """
    dictionary_not_divisible_by3 = {}
    for i in range(0,101):
        if i%3 != 0:
            dictionary_not_divisible_by3[i] = i**3
    #print(dictionary_not_divisible_by3)   


    """
    Hacer lo mismo usando dict Comprehensions:
    """
    dictionary_not_divisible_by3 = {i : i**3 for i in range(0,101) if i%3 != 0}
    #print(dictionary_not_divisible_by3)

    """
    Crear, con un dictionary comprehensions, un diccionario cuyas llaves sean los
    1000 primeros números naturales con sus raíces cuadradas como valores.
    """
    dictionary_challenge = {i: round(i**(1/2),2) for i in range(0,1001)}
    print(dictionary_challenge)
    
if __name__ == '__main__':
    run()