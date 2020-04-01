
respuesta = input('Iniciar S/N')

def obtener_datos():

    lugar = input('lugar')
    latitud = input('latitud')
    longitud = input('longitud')
    with open('estaciones.txt','a') as archivo:
        archivo.write('{:25} {:10} {:10}\n'.format(lugar, latitud, longitud)
    

def imprimir_resultados():
    with open('estaciones.txt','r') as archivo:
        print(archivo.readlines)


resp = 'S'
while (resp in ('s','S','SI','si','Si')):
    obtener_datos()
    resp = input('Otro lugar?')
imprimir_resultados()