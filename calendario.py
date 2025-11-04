#importaciones
import utiles
import equipos

#Definiciones
partidos=[]
def buscar_partido_por_id(id_partido):
    for i in partidos:
        if i["id"]==id_partido:
            return i
    return None
def crear_partido():
    jornada=utiles.leer_int("Jornada (>=1): ",1)
    local_id=utiles.leer_int("ID equipo local: ")
    visitante_id=utiles.leer_int("ID equipo visitante: ")
    if local_id==visitante_id:
        print("Un equipo no puede jugar contra sí mismo.")
        return
    local=equipos.buscar_por_id(local_id)
    visitante=equipos.buscar_por_id(visitante_id)
    if local is None or visitante is None or not local["activo"] or not visitante["activo"]:
        print("Ambos equipos deben existir y estar activos.")
        return
    fecha=input("Fecha (YYYY-MM-DD): ").strip()
    hora=input("Hora (HH:MM): ").strip()
    id_p=utiles.generar_id(partidos)
    i={"id":id_p,"jornada":jornada,"local_id":local_id,"visitante_id":visitante_id,"fecha":fecha,"hora":hora,"jugado":False,"resultado":None}
    partidos.append(i)
    print("Partido creado.")
def listar_partidos(filtro_equipo=None):
    for i in partidos:
        if filtro_equipo is None or i["local_id"]==filtro_equipo or i["visitante_id"]==filtro_equipo:
            local=equipos.buscar_por_id(i["local_id"])
            visitante=equipos.buscar_por_id(i["visitante_id"])
            estado="Jugado" if i["jugado"] else "Pendiente"
            print(i["id"],i["jornada"],local["nombre"] if local else "Desconocido",visitante["nombre"] if visitante else "Desconocido",i["fecha"],i["hora"],estado)
def reprogramar_partido():
    id_p=utiles.leer_int("ID del partido a reprogramar: ")
    i=buscar_partido_por_id(id_p)
    if i is None:
        print("Partido no encontrado.")
        return
    if i["jugado"]:
        print("No se puede reprogramar un partido jugado.")
        return
    i["fecha"]=input("Nueva fecha (YYYY-MM-DD): ").strip()
    i["hora"]=input("Nueva hora (HH:MM): ").strip()
    print("Partido reprogramado.")
def eliminar_partido():
    id_p=utiles.leer_int("ID del partido a eliminar: ")
    i=buscar_partido_por_id(id_p)
    if i is None:
        print("Partido no encontrado.")
        return
    if i["jugado"]:
        print("No se puede eliminar un partido jugado.")
        return
    partidos.remove(i)
    print("Partido eliminado.")