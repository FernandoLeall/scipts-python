#calcule o salário do funcionário com 15% de aumento
salario = float(input('Qual é o salário atual do funcionário? R$ '))
novo = salario + (salario * 15 / 100)
print('O funcionário que recebia R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}'.format(salario, novo))