viajes = []
def obtener_datos():   
    origen = input("origen: ")
    destino = input("destino: ")
    duracion = input("duracion: ")
 #  viajes.append([origen,destino,duracion]) usando listas
    viajes.append({"origen" : origen,"destino":destino,"duracion":duracion})


resp =  'S'
while(resp in 's,S,Si,SI'.split(',')):
    obtener_datos()
    resp = input('Otro viaje?')

    
archivo = open('ejemplo2.txt','r') 
print('todas las lineas :' ,archivo.readlines())
archivo.close()

with open('ejemplo2.txt','w') as archivo:
     origen,destino,duracion = obtener_datos()
     archivo.writelines('{:15} {:15} {:10}'.format(viajes(origen,destino,duracion))
     



