# Faça um programa que leia a largura e altura de uma parede em metros, calcule a área, e quantidade de tinta necessária.
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
área = largura*altura
print('Sua parede tem a dimensão de {} x {}, e sua área é de {}m²'.format(largura, altura, área))
tinta = área / 2 #cada 2m² usa 2 litros de tinta
print('Para pintar essa parede, você precisará de {}lt de tinta'.format(tinta))

