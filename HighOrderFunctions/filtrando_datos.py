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
def busqueda(name:str,data:list):
    #Esta función recibe un nombre y una lista de datos de personas.
    #La función retornara la posicion del usuario en los datos.
    pos = 0
    names = [worker["name"] for worker in DATA]
    
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
    
    
    positions_Python_devs = [busqueda(x,DATA) for x in all_python_devs]
    print(positions_Python_devs)
    Datos_python_devs = datosUsuarios(positions_Python_devs,DATA)
    
    for i in Datos_python_devs:
        print("\n")
        for key,value in i.items():
            print(key,value)
    
    

if __name__ == '__main__':
    run()