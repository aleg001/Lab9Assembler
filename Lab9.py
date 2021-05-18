#Laboratorio 9
#Realizado por: Alejandro Gómez y Marco Jurado
#Assembler
#Fecha creación: 17/05/2021
#Ultima modificación: 17/05/2021



#Se definen los imports

import RPi.GPIO as GPIO
import time 

#Se define los modos para la GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Se configura para cada salida de led
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

#Se define variable para menú:
IngresoUsuario = " "
OpcionMenu = True

#Se define función del menú:

def MenuLab9():
    print("\033[4m >>Bienvenido al Laboratorio No.9 \033[0;0m ")
    print(" Para acceder a las opciones utilice los siguientes comandos: ")
    print("   Y: para iniciar corrimiento de bits inactivos")
    print("   Q: para detener el corrimiento de bits inactivos ")

# Se define ciclo del menu
while OpcionMenu:

    MenuLab9()
    IngresoUsuario = input("Por favor, ingrese su accion: ")
     
    #Se define condiciones de inicio:
    if (IngresoUsuario == "Y" or IngresoUsuario == "y"):
        print(" >>El programa iniciara a funcionar...")
        print(" *Beeep* *Boop* *ZzzZzz* \n >>La secuencia ha iniciado: ")

        #Todas encendidas - estado inicial
        GPIO.output(3, True)
        GPIO.output(5, True)
        GPIO.output(7, True)
        GPIO.output(11, True)
        GPIO.output(13, True)
        print("*Buuuuzzzzz*")
        time.sleep(1)

        #Estado 1
        GPIO.output(13, False)
        print("*Tzzzsss*")
        time.sleep(1)


        #Estado 2
        GPIO.output(11, False)
        print("*Zaaaazzzz*")
        time.sleep(1)

        #Estado 3
        GPIO.output(7, False)
        print("*beeeeeep*")
        time.sleep(1)

        #Estado 4
        GPIO.output(5, False)
        print("*Pin Pan*")
        time.sleep(1)

        #Estado 5 - FINAL
        GPIO.output(3, False)
        #TERMINA SECUENCIA


    #Se definen condiciones de salida:
    if(IngresoUsuario == "Q" or IngresoUsuario == "q"):
        print(" >>Gracias por utilizar el programa.")
        print(" >>El corrimiento de bits inactivos se ha detenido")
        #Los puertos GPIO se limpian
        GPIO.cleanup()
        OpcionMenu = False
        
    #Se definen condiciones en caso se ingrese algo erroneo
    else:
        print(" >>Cuidado... Ese comando no existe...")

