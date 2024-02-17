import os
import modulos.regjug as r
from tabulate import tabulate
def tabnova(torneo : dict):
    info = []
    jugadores_ordenados = sorted(torneo['novato'].values(), key=lambda item: item['TP'],reverse=True)
    for jugador_info in jugadores_ordenados:
        info.append([jugador_info[key] for key in ['id','nombre','edad','PJ','PG','PP','PA','TP']])
    headers = ['ID','JUGADOR','EDAD','PJ','PG','PP','PA','TP']
    print(tabulate(info, headers=headers, tablefmt='grid'))
    jugador_max_puntos = max(torneo['novato'].values(), key=lambda x: x['TP'])
    print(f'El jugador con mas puntos de la categoria novato fue', jugador_max_puntos['nombre'])
    os.system('pause')

def tabint(torneo : dict):
    info = []
    jugadores_ordenados = sorted(torneo['intermedio'].values(), key=lambda item: item['TP'],reverse=True)
    for jugador_info in jugadores_ordenados:
        info.append([jugador_info[key] for key in ['id','nombre','edad','PJ','PG','PP','PA','TP']])
    headers = ['ID','JUGADOR','EDAD','PJ','PG','PP','PA','TP']
    print(tabulate(info, headers=headers, tablefmt='grid'))
    jugador_max_puntos = max(torneo['intermedio'].values(), key=lambda x: x['TP'])
    print(f'El jugador con mas puntos de la categoria intermedio fue', jugador_max_puntos['nombre'])
    os.system('pause')

def tabmax (torneo : dict):
    info = []
    jugadores_ordenados = sorted(torneo['avanzado'].values(), key=lambda item: item['TP'],reverse=True)
    for jugador_info in jugadores_ordenados:
        info.append([jugador_info[key] for key in ['id','nombre','edad','PJ','PG','PP','PA','TP']])
    headers = ['ID','JUGADOR','EDAD','PJ','PG','PP','PA','TP']
    print(tabulate(info, headers=headers, tablefmt='grid'))
    jugador_max_puntos = max(torneo['avanzado'].values(), key=lambda x: x['TP'])
    print(f'El jugador con mas puntos de la categoria avanzado fue', jugador_max_puntos['nombre'])
    os.system('pause')