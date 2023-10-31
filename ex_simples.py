nome = input('digite seu nome: ')
idade = input('digite sua idade: ')

if (nome and idade):
    print(nome)
    print(nome[::-1])
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}')

    if ' ' in nome:
        print('seu nome contem espaços')
    else:
        print('seu nome não contem espaços')

else:
    print('desculpe vc digitou campos vazios')
