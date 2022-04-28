lista = [1, 10]
try:
    divisao = 10 / 0
    numero = lista[1] 
    
except ZeroDivisionError:
    print('Não é possivel realizar a divisãp por zero')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritimetica')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}' .format(ex))
else:
    print('Executa quando não ocorre exceção')