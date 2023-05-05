nome = str(input('Digite o nome da pessoa: ')).upper().strip()
print('Quantas vezes aparece a letra A no nome ? {} vezes '.format(nome.count('A')))
print('A primeira letra A apareceu na posição {}'.format(nome.find('A')+1))
print('A última letra A apareceu na posição {}'.format(nome.rfind('A')+1))