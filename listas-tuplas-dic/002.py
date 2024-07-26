"""
Faça um Programa que peça as quatro notas de 5 alunos, 
calcule e armazene numa lista a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.
"""

notas = []
media_alunos = []

for i in range(5):
    notas_aluno = []
    for j in range(4):
        notas_aluno.append(float(input(f'Digite a {j+1} nota do aluno {i+1}: ')))
    media_aluno = sum(notas_aluno) / 4
    notas.append(notas_aluno)
    media_alunos.append(media_aluno)

num_alunos_maior_igual_7 = 0

for f in media_alunos:
    if f >= 7.0:
        num_alunos_maior_igual_7 += 1

print('Número de alunos com média maior ou igual a 7.0:', num_alunos_maior_igual_7)