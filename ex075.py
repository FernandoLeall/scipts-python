'''Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em um tupla. No final mostre:
A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.'''

núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes.')
if 3 in núm:
    print(f'O primeiro valor 3 foi digitado na {núm.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('O(s) número(s) pares sorteados foram', end=' ')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')





