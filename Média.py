# Calculo de Média

print = ('Calculo de média')
n1 = float(input('Nota 1 '))
n2 = float(input('Nota 2 '))
n3 = float(input('Nota 3 '))

soma = (n1 + n2 + n3)
media = soma / 3

if media > 6:
    print('Aluno Aprovado')
elif media < 6:
    print('Aluno reprovado')