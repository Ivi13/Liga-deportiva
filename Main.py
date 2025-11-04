#importaciones
import utiles
import equipos
import jugadores
import calendario
import ranking

#Definiciones
def menu_principal():
    opciones=["1.Gestión de equipos","2.Gestión de jugadores","3.Calendario y partidos","4.Resultados y clasificación","5.Salir"]
    for i in opciones:
        print(i)
    return utiles.leer_int("Elige opción: ",1)
def menu_equipos():
    opciones=["1.Crear equipo","2.Listar equipos","3.Buscar por ID","4.Actualizar","5.Eliminar","6.Volver"]
    for i in opciones:
        print(i)
    return utiles.leer_int("Elige opción: ",1)
def menu_jugadores():
    opciones=["1.Crear jugador","2.Listar jugadores","3.Buscar por ID","4.Actualizar","5.Eliminar","6.Volver"]
    for i in opciones:
        print(i)
    return utiles.leer_int("Elige opción: ",1)
def menu_partidos():
    opciones=["1.Crear partido","2.Listar partidos","3.Reprogramar","4.Eliminar","5.Volver"]
    for i in opciones:
        print(i)
    return utiles.leer_int("Elige opción: ",1)
opcion=0
while opcion!=5:
    opcion=menu_principal()
    if opcion==1:
        op=0
        while op!=6:
            op=menu_equipos()
            if op==1:
                equipos.crear_equipo()
            elif op==2:
                equipos.listar_equipos()
            elif op==3:
                id_e=utiles.leer_int("ID equipo: ")
                i=equipos.buscar_por_id(id_e)
                if i:
                    print(i)
                else:
                    print("No encontrado.")
            elif op==4:
                id_e=utiles.leer_int("ID equipo a actualizar: ")
                equipos.actualizar_equipo(id_e)
            elif op==5:
                id_e=utiles.leer_int("ID equipo a eliminar: ")
                equipos.eliminar_equipo(id_e,jugadores.jugadores_activos)
    elif opcion==2:
        op=0
        while op!=6:
            op=menu_jugadores()
            if op==1:
                jugadores.crear_jugador()
            elif op==2:
                id_f=None
                lista=input("Filtrar por equipo? (s/n): ").lower()
                if lista=="s":
                    id_f=utiles.leer_int("ID equipo: ")
                jugadores.listar_jugadores(id_f)
            elif op==3:
                id_j=utiles.leer_int("ID jugador: ")
                i=jugadores.buscar_por_id(id_j)
                if i:
                    print(i)
                else:
                    print("No encontrado.")
            elif op==4:
                id_j=utiles.leer_int("ID jugador a actualizar: ")
                jugadores.actualizar_jugador(id_j)
            elif op==5:
                id_j=utiles.leer_int("ID jugador a eliminar: ")
                jugadores.eliminar_jugador(id_j)
    elif opcion==3:
        op=0
        while op!=5:
            op=menu_partidos()
            if op==1:
                calendario.crear_partido()
            elif op==2:
                id_f=None
                lista=input("Filtrar por equipo? (s/n): ").lower()
                if lista=="s":
                    id_f=utiles.leer_int("ID equipo: ")
                calendario.listar_partidos(id_f)
            elif op==3:
                calendario.reprogramar_partido()
            elif op==4:
                calendario.eliminar_partido()
    elif opcion==4:
        op=0
        while op!=3:
            print("1.Registrar resultado\n2.Mostrar clasificación\n3.Volver")
            op=utiles.leer_int("Elige opción: ",1)
            if op==1:
                ranking.registrar_resultado()
            elif op==2:
                ranking.mostrar_clasificacion()