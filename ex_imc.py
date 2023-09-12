nome = input('Insira seu nome: ')
peso = input('peso: ')
altura = input('altura: ')

peso_num = float(peso)
altura_num = float(altura)

imc = peso_num / (altura_num**2)

if imc >= 27 and imc < 40:
    print('{}, o calculo do seu IMC é {} indica sobre peso'.format(nome, imc))

elif imc < 27 and imc > 15:
    print('{}, o calculo do seu IMC é {} indica ideal'.format(nome, imc))

elif imc < 15:
    print('{}, o calculo do seu IMC é {} indica desnutrição'.format(nome, imc))

else:
    print('{}, o calculo do seu IMC é {} indica obsidade morbidada'.format(nome, imc))

print('fim do laço')