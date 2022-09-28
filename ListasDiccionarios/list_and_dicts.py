# Listas y diccionarios Anidados.

def run():
    my_list = [1,"Hello",True,4.5]
    my_dict = { "fisrtname":"Jesus" , "lastname":"Lopez" }

    super_list = [
        {"firstname": "Facundo", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "Rodriguez"},
        {"firstname": "Pablo", "lastname": "Trinidad"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "Fernandez"},
    ]

    super_dict = {
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,4.5,6.43]
    }

    for dictionary in range(0,len(super_list)):
        if dictionary != 0:
            print("\n")
        
        for key in super_list[dictionary]:
            print(super_list[dictionary][key] + " ",end="")
    
    for key in super_dict:
        print("\n")
        print(f"{key}: ", end="")
        for numbers in super_dict[key]:
            print(numbers,end="  ")
        
    #Otra forma de acceder a los elementos:
    print("\n")
    for dictionary in super_list:
        print("\n")
        for key,value in dictionary.items():
            print(f"{value} ", end ="")

    print("\n")
    for key,value in super_dict.items():
        print(key, "-",value)

if __name__ == '__main__':
    run()