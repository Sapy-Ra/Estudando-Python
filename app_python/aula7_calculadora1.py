class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    
    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__=='__main__':
    calculadora = Calculadora(10, 2)
    print('Teste: {}' .format(calculadora.valor_a))
    print('A soma é: {}' .format(calculadora.soma()))
    print('A subtração é: {}' .format(calculadora.subtracao()))
    #print('A multiplicação é: {}' .format(calculadora.multiplicacao()))
    #print('A divisão é: {}' .format(calculadora.divisao()))
    print(f'A multiplicação é: {calculadora.multiplicacao()}')
    print(f'A Divisão é: {calculadora.divisao()}')