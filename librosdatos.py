import json
import sys


def Crearlista():
    with open("libros.txt") as arch_libro:
        listaestudiantes = []

        for lib in arch_libro:
            listaestudiantes.append(lib)

def Insertarlibro():
    with open("libros.txt",'r+') as arch_libro:
        listaestudiantes = []
        for lib in arch_libro:
            listaestudiantes.append(lib)
        listaestudiantes.append(
            ['2','desarrolloweb','wew','juan rulfo','novela','mexico''323','1990','212']
        )
    print(listaestudiantes)

def Grabarlista():
    with open("libros.txt") as arch_libro:
        listaestudiantes = []

        for lib in arch_libro:
            listaestudiantes.append(lib)

    with open("libros.json", 'w') as json_file:
        json.dump(listaestudiantes, json_file)



def menu():
    while (True):
        print("-----Menú Principal-----")
        print("1. Crear Lista")
        print("2. Insertar Libro")
        print("3. Grabar Libro")
        print("4. Salir")
        print("Selecciona una opción: ")
        try:
            opcion = int(input(""))
        except Exception as error:
            print("Error", error)
            break
        else:
            if opcion == 1:
                Grabarlista()
            elif opcion == 2:
                Insertarlibro()
            elif opcion == 3:
                Grabarlista()
            elif opcion == 4:
                break
            else:
                print("Opción incorrecta")


menu()


