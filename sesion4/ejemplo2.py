import csv
from datetime import datetime

with open('ejemplo2.csv','w') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['Nombre','Direccion','Telefono','CP', datetime.now().strftime('%c')])
    writer.writerow(['Adan', 'Dir1', 'Telefono1', 'CP2',
                     datetime.now().strftime('%c')])
    writer.writerow(['Fernando', 'Dir2', 'Telefono',
                     'CP2', datetime.now().strftime('%c')])

with open('ejemplo2.csv','r') as archivo:
    reader = csv.reader(archivo)
    for row in archivo:
        print(row)

