import time
import os
import numpy as np

concierto = np.zeros((10,10), int)

lista_rut = []
lista_totales = []
lista_pla = []
lista_gold = []
lista_silver = []
lista_cantidad = []
lista_cant_silver = []
lista_cant_pla = []
lista_cant_gold = []
lista_fila = []
lista_columna = []
acumulador_pla = 0
acumulador_gold = 0
acumulador_silver = 0
cant_entrada = lista_cantidad
cant_plata = lista_cant_pla
cant_gold = lista_cant_gold
cant_silver = lista_cant_silver

def ver_menu():
    print("""MENU
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado asistentes
    4. Mostrar ganancias totales
    5. Salir """)

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if opcion in(1,2,3,4,5):
                return opcion
            else:
                print("ERROR LA OPCION DEBE ESTAR ENTRE 1 Y 5!")
        except:
            print("ERROR DEBE INRSAR UN NUMERO ENTERO!")

def validar_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de entradas: "))
            if cantidad >= 1 and cantidad <= 3:
                return cantidad
            else:
                print("ERROR SOLO PUEDE COMPRAR MAXIMO 3 ENTRADAS!")
        except:
            print("ERROR DEBE INRSAR UN NUMERO ENTERO!")

def ver_concierto():
    os.system('cls')
    contador =1
    print("         _____________________")
    print("        |     ESENARIO        |")
    for x in range(10):
        print(f"FILA {x+1}:", end=' ')
        for y in range(10):
            print(f"{contador}", concierto[x][y], end=' ')
            contador += 1
        print( )
    print("COLUMNA     1    2    3    4    5    6    7    8    9    10")
    time.sleep(3)
    
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut: "))
            if len(str(rut))>= 7 and len(str(rut))<=8:
                return rut
            else:
                print("ERROR EL RUT DEBE TENER AL MENOS 7 U 8 DIGITOS!")
        except:
            print("ERROR DEBE INGRESAR UN NUMERO ENTERO!")

def validar_fila():
    while True:
        try:
            fila = int(input("Ingrese fila: "))
            if fila >= 1 and fila <= 10:
                return fila
            else:
                print("ERROR LA FILA DEBE ESTAR ENTRE 1 Y 10")
        except:
            print("ERROR DEBE INGRESAR UN NUMERO ENTERO")
def validar_columna():
    while True:
        try:
            columna = int(input("Ingrese columna: "))
            if columna >= 1 and columna <= 10:
                return columna
            else:
                print("ERROR LA columna DEBE ESTAR ENTRE 1 Y 10")
        except:
            print("ERROR DEBE INGRESAR UN NUMERO ENTERO")
def precios():
    print("""
    PLATINUM $120.000 (Asientos del 1 al 20)
    GOLD $80.000 (Asientos del 21 al 50)
    SILVER $50.000 (Asientos del 51 al 100)""")

def comprar_entradas():
    contador = 1
    acumulador_pla = 0
    acumulador_gold = 0
    acumulador_silver = 0

    cant_entradas = validar_cantidad()
    ver_concierto()
    precios()
    fila = validar_fila()
    columna = validar_columna()
    rut = validar_rut()
    for x in range(10):
        for y in range(10):
            if concierto[x][y]==0:
                concierto[x][y]=1
    lista_cantidad.append(cant_entradas)
    lista_fila.append(fila)
    lista_columna.append(columna)
    for x in range(10):
        for y in range(10):          
            if contador >= 1 and contador <= 20 and x in(0,1):
                acumulador_pla += 120000*cant_entradas
                lista_cant_pla.append(cant_entradas)
            elif contador >= 21 and contador <= 50 and x in(2,3,4): 
                acumulador_gold += 80000*cant_entradas
                lista_cant_gold.append(cant_entradas)
            elif contador >= 51 and contador <= 100 and x in(5,6,7,8,9):
                acumulador_silver += 50000*cant_entradas
                lista_silver.append(cant_entradas)
            else:
                print("COMPRA REALIZADA CORRECTAMENTE!")

    if rut in lista_rut:
        posicion = lista_rut.index[rut]
        lista_rut.append[posicion]
        lista_fila.append[posicion]
        lista_columna.append[posicion]
    else:
        print("NO ESTÁ DISPONIBLE")
                

def ubicaciones_disponibles():
    os.system('cls')
    rut = validar_rut()
    if rut in lista_rut:
        posicion = lista_rut.index(rut)
        ver_concierto(posicion)

def listado_asistentes():
    print("LISTA RUT: ", lista_rut)
    lista_rut.sort
    print(lista_rut)


def ganancias_totales():
    os.system('cls')
    total = lista_totales + lista_pla + lista_cant_gold + lista_silver
    print(f"""
          TIPO ENTRADA             CANTIDAD               TOTAL
    Platinum $120.000                  {cant_plata}              {acumulador_pla}
    -----------------------------------------------------------------------             
    Gold     $80.000                   {cant_gold}              {acumulador_gold}
    -----------------------------------------------------------------------
    Silver   $50.000                   {cant_silver}              {acumulador_silver}
    -----------------------------------------------------------------------
    TOTAL                              {cant_entrada}              {total} 
    -----------------------------------------------------------------------""")

def salir():
    os.system('cls')
    print("Javiera Miranda 11/07/2023")   


