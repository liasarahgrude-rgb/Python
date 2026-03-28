##Você tem uma lista de registros de notas: registros = [('Matemática', 8.5), ('História', 9.0), ('Matemática', 7.0)]. Use um laço for para converter essa lista de tuplas em um dicionário, onde as chaves são as matérias e os valores são as notas. Se houver notas duplicadas para a mesma matéria, a última nota deve ser a que prevalece. Use um set comprehension para criar um set czontendo todas as matérias únicas. Imprima o dicionário final e o set de matérias únicas.
registros = [('Matemática', 8.5), ('História', 9.0), ('Matemática', 7.0)]
dicionario = {}

for materia, nota in registros:
    # Se a matéria ainda não está no dicionário, cria uma lista vazia para ela
    if materia not in dicionario:
        dicionario[materia] = []
    # Adiciona a nota à lista daquela matéria
    dicionario[materia].append(nota)
print(dicionario)
# Resultado: {'Matemática': [8.5, 7.0], 'História': [9.0]}