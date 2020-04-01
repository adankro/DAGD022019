def obtener_datos():
    origen = input('origen?')
    destino = input('destino?')
    duracion = input('duracion?')
    return origen, destino, duracion

respuesta = 'S'
while(respuesta == 'S'):
    origen, destion, duracion = obtener_datos()
    with open('viajes.txt','a') as archivo:
        archivo.write('{:20} {:10} {:10}\n'.format(origen, destion, duracion))
    respuesta = input('Quiere agregar otro dato ?')

import csv
from datetime import datetime

with open['ejemplo2.csv','w'] as fcsv:
    write = csv.write(fcsv)
    writer.writerow(['Nombre','Direccion','Telefono','CP'])
    writer.writerow (['Marie'],'Dir1','Telefono1','CP2')

    with open ('ejempo2.csv','r') as fcsv:
        reader = cvs.reader(fcsv)


    # Reto 2 CVS 

    def obtener_datos_csv():
        Nombre_lugar = input('Nombre del Lugar?')
        Latitud = input('Latitud ?')
        Longitud = input('Longitud ?')
        Fecha_creacion = datetime.now().strftime('%HH:%MM:%SS %d:%m:%Y')

        return Nombre_lugar,Latitud,Longitud,Fecha_creacion

        respuesta == 'S'
        while (respuesta == 'S'):
            Nombre_lugar,Latitud,Logitud,Fecha_creacion = obtener_datos_csv()
            with open('Viajes_csv.csv','a') as archivocsv:
                archivocsv.write('{:30} {:15} {:15} {:15}\n'.format(Nombre_lugar,Latitud,Longitud,Fecha_creacion))
        respuesta = input('Agregamos otro?')        

# Reto 3 JASON
     
     
