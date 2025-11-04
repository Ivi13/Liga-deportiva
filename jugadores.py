#importaciones
import utiles
import equipos

#Definiciones
jugadores_activos=[]
jugadores_inactivos=[]
def crear_jugador():
    nombre=input("Nombre del jugador: ").strip()
    while nombre=="":
        print("No puede estar vacío.")
        nombre=input("Nombre del jugador: ").strip()
    posicion=input("Posición: ").strip()
    while posicion=="":
        print("No puede estar vacío.")
        posicion=input("Posición: ").strip()
    equipos.listar_equipos()
    id_equipo=utiles.leer_int("ID equipo: ")
    i=equipos.buscar_por_id(id_equipo)
    if i is None or not i["activo"]:
        print("Equipo no válido o inactivo.")
        return
    id_j=utiles.generar_id(jugadores_activos+jugadores_inactivos)
    i={"id":id_j,"nombre":nombre,"posicion":posicion,"equipo_id":id_equipo,"activo":True}
    jugadores_activos.append(i)
    print("Jugador creado.")
def listar_jugadores(filtro_equipo=None):
    for i in jugadores_activos:
        if filtro_equipo is None or i["equipo_id"]==filtro_equipo:
            e=equipos.buscar_por_id(i["equipo_id"])
            nombre_equipo=e["nombre"] if e else "Desconocido"
            print(i["id"],i["nombre"],i["posicion"],nombre_equipo)
def buscar_por_id(id_jugador):
    for i in jugadores_activos+jugadores_inactivos:
        if i["id"]==id_jugador:
            return i
    return None
def actualizar_jugador(id_jugador):
    i=buscar_por_id(id_jugador)
    if i is None:
        print("No encontrado.")
        return
    nombre=input(f"Nombre ({i['nombre']}): ").strip()
    if nombre!="":
        i["nombre"]=nombre
    posicion=input(f"Posición ({i['posicion']}): ").strip()
    if posicion!="":
        i["posicion"]=posicion
    equipos.listar_equipos()
    id_equipo=utiles.leer_int(f"Nuevo ID de equipo (actual {i['equipo_id']}): ")
    e=equipos.buscar_por_id(id_equipo)
    if e and e["activo"]:
        i["equipo_id"]=id_equipo
    print("Datos actualizados.")
def eliminar_jugador(id_jugador):
    i=buscar_por_id(id_jugador)
    if i is None:
        print("Jugador no encontrado.")
        return
    i["activo"]=False
    if i in jugadores_activos:
        jugadores_activos.remove(i)
        jugadores_inactivos.append(i)
    print("Jugador desactivado.")
