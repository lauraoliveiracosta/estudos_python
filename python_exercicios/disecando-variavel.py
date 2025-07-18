#testando o tipo privito do que foi digitado
n = input('digite algo: ')
print('É um número? ',n.isnumeric())#se é numerico
print('É alfabético? ',n.isalpha())#se é alfabetico
print('É alfanumerico: ',n.isalnum())#se é alfanumercio
print('Esta em maiusculas? ',n.isupper())#tudo maiusculo
print('Esta em minusculas? ',n.islower())#Tudo minusculo
print('Esta capitalizada? ',n.istitle())#com a primeira letra maiuscula
