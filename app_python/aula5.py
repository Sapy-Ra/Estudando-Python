lista = [12, 10, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animal[0] = 'mamaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
lista_numerica = list(tupla)
print(type(lista_numerica))

#lista.sort()
#lista_animal.sort()
#print(lista)
#print(lista_animal)
#lista_animal.reverse()
#print(lista_animal)

#nova_lista = lista_animal * 3
#print(nova_lista)

#if 'lobo' in lista_animal:
    #print('existe um gato na lsita')
#else:
    #print('não existe um lobo na lista')
    #lista_animal.append('lobo')
    #print(lista_animal)

#lista_animal.pop(0)
#print(lista_animal)

#lista_animal.remove('elefante')
#print(lista_animal)