#Laboratorio 9
#Realizado por: Alejandro Gómez y Marco Jurado
#Assembler
#Fecha creación: 17/05/2021
#Ultima modificación: 17/05/2021



#Se definen los imports

import RPi.GPIO as GPIO
import time 

#Se define los modos para la GPIO
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(PONER NUMERO, GPIO.out)

#Se define variable para menú:

IngresoUsuario = " "
OpcionMenu = True

#Se define función del menú:

def MenuLab9():
    print("Bienvenido al Laboratorio No.9")
    print("Para acceder a las opciones utilice los siguientes comandos: ")
    print(" Y: para iniciar corrimiento de bits inactivos")
    print(" Q: para detener el corrimiento de bits inactivos ")

# Se define ciclo del menu
while OpcionMenu:

    MenuLab9()
    IngresoUsuario = input("Por favor, ingrese su accion: ")

    #Se define condiciones de inicio:
    if (IngresoUsuario == "Y"):
        print("El programa iniciara a funncionar...")
        print("El corrimiento de bits ha iniciado: ")

    #Se definen condiciones de salida:
    if(IngresoUsuario == "Q"):
        print("Gracias por utilizar el programa.")
        print("El corrimiento de bits inactivos se ha detenido")
        OpcionMenu = False
        
    #Se definen condiciones en caso se ingrese algo erroneo
    else:
        print("Cuidado... Ese comando no existe...")