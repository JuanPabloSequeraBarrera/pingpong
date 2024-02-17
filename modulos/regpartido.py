import os 
import modulos.menu as menu
def validacionjug(torneo : dict):
    os.system('cls')
    isActive = True
    while isActive:
        print(menu.titulo)
        print('Bienvenido al registro de partidos, porfavor seleccione la categoria para el registro de partido')
        opciones = ('1.NOVATO\n2.INTERMEDIO\n3.AVANZADO\n4.SALIR')
        print(opciones)
        try:
            op = int(input(':)_ '))
            if (op == 1):
                partidonov(torneo)
            elif (op == 2):
                partidoint(torneo)
            elif (op ==3):
                partidoavanz(torneo)
            elif (op == 4):
                isActive = False
                return
            else:
                print('Dato no valido')
                os.system('pause')
                os.system('cls')
        except ValueError:
            print('Error de digitacion')
            os.system('pause')
            validacionjug(torneo)

def partidonov(torneo:dict):
    os.system('cls')
    if (len(torneo['novato']) >= 5):
        try:
            print('Escriba el ID del jugador 1')
            player1 = int(input(':)_ '))
            print('Escriba el ID del jugador 2')
            player2 = int(input(':)_ '))
            if player1 in torneo['novato'] and player2 in torneo['novato']:
                print(f'Cual fue el puntaje de {player1} ')
                m1 = int(input(':)_'))
                print(f'Cual fue el puntaje de {player2} ')
                m2 = int(input(':)_'))
                if m1>m2:
                    torneo['novato'][player1]['PJ'] = 1
                    torneo['novato'][player2]['PJ'] = 1
                    torneo['novato'][player1]['PG'] = 1
                    torneo['novato'][player2]['PP'] = 1
                    torneo['novato'][player1]['PA'] = (m1 - m2)
                    torneo['novato'][player1]['TP'] = 2
                elif m2>m1:
                    torneo['novato'][player1]['PJ'] = 1
                    torneo['novato'][player2]['PJ'] = 1
                    torneo['novato'][player2]['PG'] = 1
                    torneo['novato'][player1]['PP'] = 1
                    torneo['novato'][player2]['PA'] = (m2 - m1)
                    torneo['novato'][player2]['TP'] = 2
                else:
                    torneo['novato'][player1]['PJ'] = 1
                    torneo['novato'][player2]['PJ'] = 1
                    torneo['novato'][player1]['TP'] = 1
                    torneo['novato'][player2]['TP'] = 2
            else:
                print('Jugadores no registrados')
                os.system('pause')
                return
        except ValueError:
            print('Dato invalido')
            os.system('pause')
            partidonov(torneo)
        else:
         print('El partido y la asignacion de puntos se ha hecho satisfactoriamente, desea agregar un nuevo encuentro? Si(si) No(no)')
         des = str(input(':)_')).upper()
         if des == 'NO':
             os.system('pause')
             return
         else:
             partidonov(torneo)    
    else:
        print('No hay suficientes jugadores registrados para iniciar los juegos, minimo 5')
        return
    
def partidoint(torneo:dict):
    os.system('cls')
    if (len(torneo['intermedio']) >= 5):
        try:
            print('Escriba el ID del jugador 1')
            player1 = int(input(':)_ '))
            print('Escriba el ID del jugador 2')
            player2 = int(input(':)_ '))
            if player1 in torneo['intermedio'] and player2 in torneo['intermedio']:
                print(f'Cual fue el puntaje de {player1}')
                m1 = int(input(':)_'))
                print(f'Cual fue el puntaje de {player2}')
                m2 = int(input(':)_'))
                if m1>m2:
                    torneo['intermedio'][player1]['PJ'] = 1
                    torneo['intermedio'][player2]['PJ'] = 1
                    torneo['intermedio'][player1]['PG'] = 1
                    torneo['intermedio'][player2]['PP'] = 1
                    torneo['intermedio'][player1]['PA'] = (m1 - m2)
                    torneo['intermedio'][player1]['TP'] = 2
                elif m2>m1:
                    torneo['intermedio'][player1]['PJ'] = 1
                    torneo['intermedio'][player2]['PJ'] = 1
                    torneo['intermedio'][player2]['PG'] = 1
                    torneo['intermedio'][player1]['PP'] = 1
                    torneo['intermedio'][player2]['PA'] = (m2 - m1)
                    torneo['intermedio'][player2]['TP'] = 2
                else:
                    torneo['intermedio'][player1]['PJ'] = 1
                    torneo['intermedio'][player2]['PJ'] = 1
                    torneo['intermedio'][player1]['TP'] = 1
                    torneo['intermedio'][player2]['TP'] = 2
            else:
                print('Jugadores no registrados')
                os.system('pause')
                return
        except ValueError:
            print('Dato invalido')
            os.system('pause')
            partidonov(torneo)
        else:
         print('El partido y la asignacion de puntos se ha hecho satisfactoriamente, desea agregar un nuevo encuentro? Si(si) No(no)')
         des = str(input(':)_')).upper()
         if des == 'NO':
             os.system('pause')
             return
         else:
             partidonov(torneo)    
    else:
        print('No hay suficientes jugadores registrados para iniciar los juegos, minimo 5')
        return
    
def partidoavanz(torneo:dict):
    os.system('cls')
    if (len(torneo['avanzado']) >= 5):
        try:
            print('Escriba el ID del jugador 1')
            player1 = int(input(':)_ '))
            print('Escriba el ID del jugador 2')
            player2 = int(input(':)_ '))
            if player1 in torneo['avanzado'] and player2 in torneo['avanzado']:
                print(f'Cual fue el puntaje de {player1}')
                m1 = int(input(':)_'))
                print(f'Cual fue el puntaje de {player2}')
                m2 = int(input(':)_'))
                if m1>m2:
                    torneo['avanzado'][player1]['PJ'] = 1
                    torneo['avanzado'][player2]['PJ'] = 1
                    torneo['avanzado'][player1]['PG'] = 1
                    torneo['avanzado'][player2]['PP'] = 1
                    torneo['avanzado'][player1]['PA'] = (m1 - m2)
                    torneo['avanzado'][player1]['TP'] = 2
                elif m2>m1:
                    torneo['avanzado'][player1]['PJ'] = 1
                    torneo['avanzado'][player2]['PJ'] = 1
                    torneo['avanzado'][player2]['PG'] = 1
                    torneo['avanzado'][player1]['PP'] = 1
                    torneo['avanzado'][player2]['PA'] = (m2 - m1)
                    torneo['avanzado'][player2]['TP'] = 2
                else:
                    torneo['avanzado'][player1]['PJ'] = 1
                    torneo['avanzado'][player2]['PJ'] = 1
                    torneo['avanzado'][player1]['TP'] = 1
                    torneo['avanzado'][player2]['TP'] = 2
            else:
                print('Jugadores no registrados')
                os.system('pause')
                return
        except ValueError:
            print('Dato invalido')
            os.system('pause')
            partidonov(torneo)
        else:
         print('El partido y la asignacion de puntos se ha hecho satisfactoriamente, desea agregar un nuevo encuentro? Si(si) No(no)')
         des = str(input(':)_')).upper()
         if des == 'NO':
             os.system('pause')
             return
         else:
             partidonov(torneo)    
    else:
        print('No hay suficientes jugadores registrados para iniciar los juegos, minimo 5')
        return