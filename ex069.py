tot18 = totH = totM20 = 0
while True:
    idade = int(input("Digite a idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo {M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Você quer continuar? {S/N]')).strip().upper()[0]
    if continua not in 'Ss':
        break
print(f'Total de pessoas com mais de 18 anos é de {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'Temos {totM20} mulheres com menos de 20 anos')


