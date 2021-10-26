import numpy as np
from collections import namedtuple

tablero = np.array([[" "]*8]*8) # aprovechamos las funciones de la librería NumPy para crear una matriz de 8 x 8 inicializada en False 

PosicionTablero = namedtuple('PosicionTablero',['f','c']) # Definimos una tupla para la posición de la torre


def ataque_torre(tablero,posicion):
  for i in range(0,8):   #asigna la fila
    tablero[posicion.f,i]=1

  for i in range(0,8): #asigna la columna
    tablero[i,posicion.c]=1
    
  tablero[posicion.f, posicion.c]=0

def ataque_reina(tablero, posicion):
  print(f"({posicion.f},{posicion.c} )")
  for i in range(0,8):#asigna la fila
    #Diagonales principales arriba y abajo
      if (posicion.f+i)<8 and (posicion.c+i)<8:
          tablero[(posicion.f+i),(posicion.c+i)]=1
      if (posicion.c-i)>=0 and (posicion.f-i)>=0:
          tablero[(posicion.f-i),(posicion.c-i)]=1
    #Diagonales secunadrias arriba y abajo
      if (posicion.f+i)<8 and (posicion.c-i)>=0:
          tablero[(posicion.f+i),(posicion.c-i)]=1          
      if (posicion.f-i)>=0 and (posicion.c+i)<8:
          tablero[(posicion.f-i),(posicion.c+i)]=1
    #Asigna la fila
      tablero[posicion.f,i]=1
    #Asigna la columna
      tablero[i,posicion.c]=1
      
  tablero[posicion.f, posicion.c]=0
    
def ataque_alfil(tablero, posicion):
  print(f"({posicion.f},{posicion.c} )")
  for i in range(0,8):#asigna la fila
    #Diagonales principales arriba y abajo
      if (posicion.f+i)<8 and (posicion.c+i)<8:
          tablero[(posicion.f+i),(posicion.c+i)]=1
      if (posicion.c-i)>=0 and (posicion.f-i)>=0:
          tablero[(posicion.f-i),(posicion.c-i)]=1
    #Diagonales secunadrias arriba y abajo
      if (posicion.f+i)<8 and (posicion.c-i)>=0:
          tablero[(posicion.f+i),(posicion.c-i)]=1          
      if (posicion.f-i)>=0 and (posicion.c+i)<8:
          tablero[(posicion.f-i),(posicion.c+i)]=1
    
  tablero[posicion.f, posicion.c]=0

def ataque_caballo(tablero, posicion):
    print(f"({posicion.f},{posicion.c} )")
  
    if posicion.c-2>=0:
        if posicion.f-1>=0:
            tablero[posicion.f-1,posicion.c-2]=1
        if posicion.f+1<8:
            tablero[posicion.f+1,posicion.c-2]=1
        if posicion.c-1>=0:  
            if posicion.f-2>=0:
                tablero[posicion.f-2,posicion.c-1]=1
            if posicion.f+2<8:
                tablero[posicion.f+2,posicion.c-1]=1
        if posicion.c+1<8:
            if posicion.f-2>=0:
                tablero[posicion.f-2,posicion.c+1]=1
            if posicion.f+2<8:
                tablero[posicion.f+2,posicion.c+1]=1
           
    if posicion.c+2<8:
        if posicion.f-1>=0:
            tablero[posicion.f-1,posicion.c+2]=1
        if posicion.f+1<8:
            tablero[posicion.f+1,posicion.c+2]=1
        if posicion.c-1>=0:
            if posicion.f-2>=0:
                tablero[posicion.f-2,posicion.c-1]=1
            if posicion.f+2<8:
                tablero[posicion.f+2,posicion.c-1]=1
        if posicion.c+1<8:
            if posicion.f-2>=0:
                tablero[posicion.f-2,posicion.c+1]=1
            if posicion.f+2<8:
                tablero[posicion.f+2,posicion.c+1]=1
 
    tablero[posicion.f, posicion.c]=0

def ataque_peon(tablero, posicion):
    print(f"({posicion.f},{posicion.c} )")
  
    print("""
    [1]  Peon Blanco
    [2]  Peon Negro
    """)
    x= int(input("Elija un color de peon:  "))
    
    if x==1:
        tablero[posicion.f-1, posicion.c-1]=1
        tablero[posicion.f-1, posicion.c+1]=1
    elif x==2:
        tablero[posicion.f+1, posicion.c-1]=1
        tablero[posicion.f+1, posicion.c+1]=1
 
    tablero[posicion.f, posicion.c]=0

def ataque_rey(tablero, posicion):
    print(f"({posicion.f},{posicion.c} )")
    
    #if posicion.c-1>=0:
    if posicion.f-1>=0:
        tablero[posicion.f-1, posicion.c]=1
        if posicion.c+1<8:
            tablero[posicion.f-1, posicion.c+1]=1
        if posicion.c-1>=0:
            tablero[posicion.f-1, posicion.c-1]=1
    if posicion.f+1<8:
        tablero[posicion.f+1, posicion.c]=1
        if posicion.c-1>=0:
            tablero[posicion.f+1, posicion.c-1]=1
        if posicion.c+1<8:
            tablero[posicion.f+1, posicion.c+1]=1
    if posicion.c-1>=0:
        tablero[posicion.f, posicion.c-1]=1
    if posicion.c+1<8:
        tablero[posicion.f, posicion.c+1]=1
    
    
    tablero[posicion.f, posicion.c]=0
    

while True:
    fil= int(input("Elija la fila en la que se ubica la pieza (0 a 7):  "))
    col= int(input("Elija la columna en la que se ubica la pieza (0 a 7):  "))
    
    posicion=PosicionTablero(fil,col)
    print("""
    [1] POSICIONES DE TORRE
    [2] POSICIONES DE REINA
    [3] POSICIONES DE ALFIL     
    [4] POSICIONES DE CABALLO
    [5] POSICIONES DE PEON
    [6] POSICIONES DE REY
    
    """)
    
    w = input("Elija un opcion:  ")
    
    if w=="1":
        ataque_torre(tablero,posicion)   
    elif w=="2":
        ataque_reina(tablero,posicion)   
    elif w=="3":
        ataque_alfil(tablero,posicion)  
    elif w=="4":
        ataque_caballo(tablero, posicion)
    elif w=="5":
        ataque_peon(tablero, posicion)   
    elif w=="6":
        ataque_rey(tablero, posicion)
    else:
        print("Elija una opcion valida")
        
    
    print(tablero)

"""
Desarrolla las funciones para las demas figuras

Reina
Alfil
Caballo
Peon
Rey
"""
