DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def busquedaPorNombre(name:str,data:list):
    #Esta función recibe un nombre y una lista de datos de personas.
    #La función retornara la posicion del usuario en los datos.
    pos = 0
    names = [worker["name"] for worker in DATA]
    #info_workter = list(filter(lambda worker: worker["name"] == name,data))
    #print(asd)
    for i in names:
        if name == i:
            return pos
        else:
            pos += 1
        
def datosUsuarios(positions:list,data:list):
    datosUsuarios = [data[x] for x in positions]
    return datosUsuarios

def run():
    #Obtener una lista de los trabajadores, cuyo lenguaje de programación es python.
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    #Obtener una lista de los trabajadores, cuya organización es Platzi.
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    #Obtener una lista de los trabajores que saben python y trabajan en Platzi.
    all_Python_Platzi_devs = [worker["name"] for worker in DATA if worker["language"] == "python" and worker["organization"] == "Platzi"]
    
    
    positions_Python_devs = [busquedaPorNombre(x,DATA) for x in all_python_devs]
    print(positions_Python_devs)
    Datos_python_devs = datosUsuarios(positions_Python_devs,DATA)
    
    for i in Datos_python_devs:
        print("\n")
        for key,value in i.items():
            print(key,value)
    
    adults = list(filter(lambda worker: worker["age"] > 18,DATA))
    adults = list(map(lambda worker: worker["name"],adults))
    
    #old_people = list(map(lambda worker : worker | {"old" : worker["age"] > 70},DATA))
    
    """Reto.
    1) Crear las listas all_python_devs y all_platzi_workers usando una combinacion 
    de filter y map.
    
    2) Crear la lista old_people y aduls con list comprehensions.
    """

    #1)
    all_python_devs = list(filter(lambda worker:worker["language"] == "python",DATA))
    all_python_devs = list(map(lambda worker:worker["name"],all_python_devs))
    
    all_Platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi",DATA))
    all_Platzi_workers = list(map(lambda worker: worker["name"],all_Platzi_workers))
    
    #2)
    old_people = {}
    adults = [worker["name"] for worker in DATA if worker["age"] >18]

if __name__ == '__main__':
    run()