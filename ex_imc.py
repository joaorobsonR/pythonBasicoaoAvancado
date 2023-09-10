nome = input(str('Insira seu nome: '))
peso = 80
altura = 1.74
imc = peso / (altura * altura)

print('{}, o calculo do seu IMC é {}'.format(nome, imc))
print(f'{nome} seu IMC é {imc:.2f}')