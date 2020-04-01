import json
import  requests 

with open('ejemplo.json') as  archivo:
    diccionario = json.loads(archivo.read())
    
diccionario['nueva_clave'] = 25

with open('ejemplo2.json','w') as ejemplo:
    ejemplo.write(json.dumps(diccionario, indent=4))

reponse = requests.get('https://pokeapi.co/api/v2/pokemon/ditto/')

ditto = json.loads(reponse.text)
print(ditto['abilities'])
