a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado = ('soma: {soma}. \nsubtracao: {sub}.' 
'\nmultiplicacao: {multi}.' 
'\ndivisao: {div}.' 
'\nresto: {resto}' .format(soma=soma, 
                           sub = subtracao, 
                           multi = multiplicacao,
                           div = divisao,
                           resto = resto))
print(resultado) 

#x = '1'
#soma2 = int(x) + 1
#print('soma 2:', soma2)