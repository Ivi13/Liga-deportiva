#Definiciones
def generar_id(lista):
    if not lista:
        return 1
    return max(i["id"] for i in lista)+1
def leer_int(mensaje,minimo=None):
    valor=input(mensaje)
    valido=True
    for i in valor:
        if i not in "0123456789":
            valido=False
    if not valido or valor=="":
        print("Introduce un número válido.")
        return leer_int(mensaje,minimo)
    numero=int(valor)
    if minimo is not None and numero<minimo:
        print(f"El número debe ser ≥ {minimo}.")
        return leer_int(mensaje,minimo)
    return numero
def buscar_por_id(eleccion,lista):
    for i in lista:
        if i["id"]==eleccion:
            return i
    return None

