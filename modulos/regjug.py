import os
import modulos.menu as menu
def regjugador(torneo: dict):
    print(menu.titulo)
    print('Bienvenido al registro de jugadores del torneo de Tenis de Mesa, por favor ingrese su ID')
    try:
        id = int(input(':)_ '))
        if id in torneo['novato'] or id in torneo['intermedio'] or id in torneo['avanzado']:
            print('Jugador ya registrado')
            os.system('pause')
            return
        print('Por favor ingrese su nombre')
        nombre = str(input(':)_ ').upper())
        print('Por favor ingrese su edad')
        edad = int(input(':)_ ')) 
        jugador = {
            'id': id,
            'nombre': nombre,
            'edad': edad,
            'PJ': 0,
            'PG': 0,
            'PP': 0,
            'PA': 0,
            'TP': 0       
        }
        if (edad >= 15) and (edad <= 16):
            torneo['novato'][id] = jugador
        elif (edad >= 17) and (edad <= 20):
            torneo['intermedio'][id] = jugador
        elif (edad > 20):
            torneo['avanzado'][id] = jugador
        else:
            print('El jugador registrado no cumple con la edad mínima de participación')
            os.system('pause')
            return
    except ValueError:
        print('Dato inválido')
        os.system('pause')
    else:
        print('Jugador registrado correctamente')
        print('Desea registrar otro jugador? Si(si) No(no)')
        des = str(input(':)_ ').upper())
        if des == 'NO':
            os.system('pause')
        else:
            os.system('cls')
            regjugador(torneo)
