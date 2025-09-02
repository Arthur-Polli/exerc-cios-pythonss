n01 = int(input('primeira nota do aluno: '))
n02 = int(input('segunda nota do aluno: '))

n03 = n01 + n02
n04 = n03 / 2

print(f'então a média do seu aluno é: {n04}')

if n04 > 5:
   print('você está aprovado')
else:
   print('você foi reprovado')