#importaciones
import utiles

#Definiciones
equipos_activos=[]
equipos_inactivos=[]
def crear_equipo():
    nombre=input("Nombre del equipo: ").strip()
    while nombre=="":
        print("No puede estar vacío.")
        nombre=input("Nombre del equipo: ").strip()
    ciudad=input("Ciudad del equipo: ").strip()
    while ciudad=="":
        print("No puede estar vacío.")
        ciudad=input("Ciudad del equipo: ").strip()
    id_equipo=utiles.generar_id(equipos_activos+equipos_inactivos)
    i={"id":id_equipo,"nombre":nombre,"ciudad":ciudad,"activo":True}
    equipos_activos.append(i)
    print("Equipo creado correctamente.")
def listar_equipos():
    for i in equipos_activos:
        print(i["id"],i["nombre"],i["ciudad"])
def buscar_por_id(id_equipo):
    for i in equipos_activos+equipos_inactivos:
        if i["id"]==id_equipo:
            return i
    return None
def actualizar_equipo(id_equipo):
    i=buscar_por_id(id_equipo)
    if i is None:
        print("No encontrado.")
        return
    nombre=input(f"Nombre ({i['nombre']}): ").strip()
    if nombre!="":
        i["nombre"]=nombre
    ciudad=input(f"Ciudad ({i['ciudad']}): ").strip()
    if ciudad!="":
        i["ciudad"]=ciudad
    print("Datos actualizados.")
def eliminar_equipo(id_equipo,jugadores_activos):
    i=buscar_por_id(id_equipo)
    if i is None:
        print("No encontrado.")
        return
    hay_jugadores=False
    for j in jugadores_activos:
        if j["equipo_id"]==id_equipo:
            hay_jugadores=True
    if hay_jugadores:
        print("No se puede eliminar un equipo con jugadores activos.")
        return
    i["activo"]=False
    if i in equipos_activos:
        equipos_activos.remove(i)
        equipos_inactivos.append(i)
    print("Equipo desactivado.")
