import os
import modulos.menu as menu
import modulos.regjug as reg
import modulos.regpartido as r
import modulos.tabla as t
torneo = {
    'novato':{

    },
    'intermedio':{

    },
    'avanzado':{

    }
}
isActive = True 
while isActive:
    os.system('cls')
    op = menu.menu()
    if (op == 1):
        reg.regjugador(torneo)
    if (op == 2):
        r.validacionjug(torneo)
    if (op == 3):
        t.tabnova(torneo)
    if (op == 4):
        pass
    if (op == 5):
        isActive = False
        print('Muchas gracias por hacer uso del software')
        os.system('pause')