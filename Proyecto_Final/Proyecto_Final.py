#Hacer un menu de registro que prgunte nombre, contra, y una pregunta personal.
##Que cuando ingrese, el programa diga "el usuario se creo correctamente"
#Que guarde los datos ingresados
#Que muestre los datos

#Importando modulo para ocultar la clave
import getpass

#importando herramientas para manejo de archivos
from io import open

#Se define la funcion de menu
def Menu():
    while True:
        opc = int(input("-------------Menu-------------\n1. Nuevo registro\n2. Mostrar registros\n3. Salir\n-->"))

        if opc is 1:

            print("\n********Nuevo registro********\n")
            #se abre el archivo de modo que pueda agregar varios datos
            file = open("storage.txt","a")

            name = input("Ingresa un nombre--> ")
            #Metodo para ocultar clave
            passw = getpass.getpass("Introduce la contraseña-->")
            pp = input("Como se llama tu mascota?-->")

            print("\nEl usuario: ", name, " se ha guardado exitosamente\n")

            #Se escriben los datos en el archivo previamente definido
            file.write(name)
            file.write("||")
            file.write(passw)
            file.write("||")
            file.write(pp)
            file.write("\n")    
            file.close
        
        elif opc is 2:
            file = open("storage.txt", "r")
            
            show = file.read()
            file.close()

            print(show)
        
        elif opc is 3:
            print("Gracias por utilizar nuestro sistema, vuela pronto")
            break
            


Menu()

