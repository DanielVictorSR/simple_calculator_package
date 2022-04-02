from calculator import Calc

##instanciando a classe Calc
calc = Calc()


##interface com o usuario e chamada de operacoes (calc)
def main():
      ##detalhes de funcionamento
      div_text = 45*'#'
      print('\n'+div_text+'\nSimple Calculator\n'
            'Operations Allowed\n'
            '+ (sum) - (subtract) * (multiply) / (divide)\n'
            +div_text+'\n'
            'Just once operator per time\n'
            'eg.: 10+10+10+10 or 20-20-20-20 ...\n'
            +div_text+'\n')

      ##solicitando dados do usuário
      operation = input('Enter with a expression: ')

      ##organizando dados
      ###encontrando operador
      operator = operation.find('+')

      count = 0
      while (operator == -1):
            count += 1

            if count == 1:
                  operator = operation.find('-')

            if count == 2:
                  operator = operation.find('*')

            if count == 3:
                  operator = operation.find('/')

      ###removendo operador dos números e gerando lista (str)
      operation2 = operation.split(operation[operator])           #operation2 devido identificar operador

      ###identificando operador
      operator = operation[operator]

      ###convertendo str >> float
      float_numbers = [int(i) for i in operation2]

      ##realizando chamadas das funções
      if operator == '+':
            calc.sum(float_numbers)
      if operator == '-':
            calc.subtract(float_numbers)
      if operator == '*':
            calc.multiply(float_numbers)
      if operator == '/':
            calc.divide(float_numbers)


if __name__ == '__main__':
      main()
      again = input('Do you want do a new calc?\n Y - Yes or anyother to exit: ')
      if again == 'Y' or again == 'y':
            main()
      else:
            exit()