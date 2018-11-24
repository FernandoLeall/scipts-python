#Faça um programa que calcule o valor de um produto considerando a forma de pagamento.
print('{:=^40}'.format(' LEAL MAGAZINE '))
preço = float(input('Valor das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] Á vista dinheiro/cheque
[ 2 ] Á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual a opção de pagamento? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas: '))
    parcela = total /totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('Opção errada de pagamento, tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))




