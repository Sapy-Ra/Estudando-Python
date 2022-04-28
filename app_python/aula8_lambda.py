contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
contador_letras(lista_animais)
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
print(soma(5, 10)) 

sub = lambda a, b: a - b
print(sub(10, 5)) 

calculadora = {
    'soma': lambda a, b : a + b,
    'sub': lambda a, b : a - b,
    'multi': lambda a, b : a * b,
    'div': lambda a, b : a / b,
}

print(type(calculadora))
soma = calculadora['soma']
multi = calculadora['multi']
print('A soma é: {}' .format(soma(10, 5)))
print('A multiplicação é: {}' .format(multi(10, 2)))