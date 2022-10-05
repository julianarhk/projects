peso = float(input('Qual é o seu peso em kg? '))
altura = float(input('Qual é a sua altura em metros? '))
imc = peso / (altura ** 2)


if imc < 18.5:
    print(f'Seu imc é: {imc}, você está abaixo do peso.')
elif  18.5 <= imc <=25:
    print(f'Seu imc é: {imc}, você está no peso ideal!')
elif 25 < imc <= 30:
    print(f'Seu imc é: {imc}, você está com sobreso.')
elif 30 < imc <= 40:
    print(f'Seu imc é: {imc}, você está obeso(a).')
else:
    print(f'Seu imc é: {imc}, você está com obesidade mórbida.')
