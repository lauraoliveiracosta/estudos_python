'''
ESTE CÓDIGO NÃO FUNCIONA, POIS O '+' NO CÓDIGO CONCATENA OS VALORES AO INVES DE SOMAR

n1 = input('Digite um numero')
n2 = input('Digite outro numero:')
s=(n1+n2)
print('A soma vale:',n2)

Tipos primitivos:
Int: 7 | -4 0 | 9875
flooat: 4.5 | 0.076 | -15.223 | 7.0
bool: true |false
str: 'Ola' | '7.5' | ''

Precisa definir o tipo de dado que sera inserido no input
'''
n1 = int(input ('Digite um Numero: ') )
n2 = int(input('Digite outro numero: '))
s = n1+n2
print('A soma dos valores é',s)
print('A soma vale: {}'.format(s)) #Outra forma de fazer um print com a mascara format
print('A soma entre {} e {} vale {}'.format(n1,n2,s))#Ainda usando o format para puxar variavel para dentro da string do print.
print(f'A soma entre {n1} e {n2} vale {s}')#Forma mais atualizada para usar o format


