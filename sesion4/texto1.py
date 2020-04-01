with open('ejemplo1.txt','w') as archivo:
    archivo.write('Primera Linea\t')
    archivo.writelines(['Segunda Linea\n','Tercera Linea\n','Cuarta Linea\n','Quinta\n'])
    print('Dentro del with')

print('Furea del with')

with open('ejemplo1.txt') as archivo:
    print('primera linea: ', archivo.readline())
    print('segunda linea: ', archivo.readline())
    print('Todas laslineas: ', archivo.readlines())


# Prueba de que Fer es programador tambien mau

with open('FerAlmaraz.txt','w') as archivo:
    archivo.writelines('Lugar\t','Longitud\t','Latidud' )
    '{:25} {:10} {:10}\n'.format(lugar, ubicacion, precio)