nome = str(input('Digite o nome do aluno: '))
nota = int(input('Digite uma nota: '))
pergunta = str(input('Deseja digitar uma nova nota?(s/n): '))

ciclo = 1
while pergunta == 's':
    nova_nota = int(input('Digite a outra nota: '))
    nota = nova_nota + nota
    pergunta = str(input('Deseja digitar uma nova nota?(s/n): '))
    ciclo += 1

if nota / ciclo >= 5:
    print (f'{nome} foi aprovado!')
else:
    print(f'{nome} foi reprovado!')
print (f' sua média foi {nota/ciclo}')