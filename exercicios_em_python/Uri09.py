#Exercicio 9 - Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário.
#A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

NUM_1 = int(input(''))
NUM_2 = int(input(''))
NUM_3 = float(input(''))

SALARY = NUM_2 * NUM_3

print('NUMBER = {}'.format(NUM_1))
print('SALARY = U$ {:.2f}'.format(SALARY))