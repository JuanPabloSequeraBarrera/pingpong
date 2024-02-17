import os
titulo = """
    +++++++++++++++++++++++++++++++++++++++++++
    +Registro torneo tenis de mesa CAMPUS 2024+
    +++++++++++++++++++++++++++++++++++++++++++
""" 
lstopciones = [1,2,3,4,5]
opciones = ('1.Registro de Jugador\n2.Registro de partido jugado\n3.Tabla de Posiciones\n4.Ganadores por Categoria\n5.Salir')
def menu():
    os.system('cls')
    print(titulo)
    print(opciones)
    try:
        op = int (input(':)_ '))
        if (not op in lstopciones):
            print('numero no valido')
            os.system('pause')
            menu()
    except ValueError:
        print('Error en el dato ingresado')
        os.system('pause')
        menu()
    else:
        return op