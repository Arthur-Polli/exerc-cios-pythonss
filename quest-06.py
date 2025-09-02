print('=======================')
print('olha os horarios massa demais rs')
print('=======================')

idade = int(input('digite sua idade '))

if idade < 16:
   print('você ainda não pode votar, senhorzinho')

elif 18 < idade < 65: 
   print('seu voto é opicional, senhor(a).')
else:
   print('seu voto é obrigatório senhor(a).')