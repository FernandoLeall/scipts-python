#Faça um programa que leia o preço de um produtos e calcule um novo preço com 5% de desconto.
preço = float(input('Quanto custa o produto? R$  '))
novo = preço - (preço * 5 / 100)
print('O produto que custava R$ {:.2f}, na promoção custará R$ {:.2f}'.format(preço, novo))
