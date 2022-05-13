aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
elif 7 > aluno['media'] >= 5:
    aluno['situacao'] = 'recuperação'
else:
    aluno['situacao'] = 'reprovado'

print(f'Nome = {aluno["nome"]}\n'
      f'Média = {aluno["media"]}\n'
      f'Situação = {aluno["situacao"]}')
