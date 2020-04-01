import csv

respuesta = input('Iniciar S/N')

def obtener_datos():

    lugar = input('lugar')
    latitud = input('latitud')
    longitud = input('longitud')
    with open('estaciones.csv','a') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['{:},{:},{:},{:}'.format(lugar, latitud, longitud, datetime.now().strftime('%c')])


def imprimir_resultados():
    with open('estaciones.csv','r') as archivo:
    reader = csv.reader(archivo)
    for row in archivo:
        print(row)


resp = 'S'
while (resp in ('s','S','SI','si','Si')):
    obtener_datos()
    resp = input('Otro lugar?')
imprimir_resultados()