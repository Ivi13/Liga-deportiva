#importaciones
import calendario
import equipos
import utiles

#Definiciones
def registrar_resultado():
    id_p=utiles.leer_int("ID del partido a registrar: ")
    i=calendario.buscar_partido_por_id(id_p)
    if i is None:
        print("Partido no encontrado.")
        return
    if i["jugado"]:
        print("Partido ya registrado.")
        return
    gL=utiles.leer_int("Goles local: ",0)
    gV=utiles.leer_int("Goles visitante: ",0)
    i["resultado"]=(gL,gV)
    i["jugado"]=True
    print("Resultado registrado.")
def mostrar_clasificacion():
    tabla={}
    for i in equipos.equipos_activos:
        tabla[i["id"]]={"nombre":i["nombre"],"PJ":0,"G":0,"E":0,"P":0,"GF":0,"GC":0,"PTS":0}
    for i in calendario.partidos:
        if i["jugado"]:
            local=i["local_id"]
            visitante=i["visitante_id"]
            gL,gV=i["resultado"]
            tabla[local]["PJ"]+=1
            tabla[visitante]["PJ"]+=1
            tabla[local]["GF"]+=gL
            tabla[local]["GC"]+=gV
            tabla[visitante]["GF"]+=gV
            tabla[visitante]["GC"]+=gL
            if gL>gV:
                tabla[local]["G"]+=1
                tabla[visitante]["P"]+=1
                tabla[local]["PTS"]+=3
            elif gL<gV:
                tabla[visitante]["G"]+=1
                tabla[local]["P"]+=1
                tabla[visitante]["PTS"]+=3
            else:
                tabla[local]["E"]+=1
                tabla[visitante]["E"]+=1
                tabla[local]["PTS"]+=1
                tabla[visitante]["PTS"]+=1
    lista=[]
    for i in tabla:
        t=tabla[i]
        lista.append([t["nombre"],t["PJ"],t["G"],t["E"],t["P"],t["GF"],t["GC"],t["PTS"]])
    for i in lista:
        print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
