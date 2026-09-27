notas = []

for i in range(30):
    while True:
        try:
            nota = float(input(f"Digite a nota do aluno {i + 1} (entre 0 e 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Nota inválida! Por favor, insira um valor de 0 a 10.")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

# Relatório Final
media = sum(notas) / len(notas)
maior_nota = max(notas)
menor_nota = min(notas)

print("\n" + "=" * 30)
print("RELATÓRIO FINAL")
print("=" * 30)
print(f"Total de notas registradas: {len(notas)}")
print(f"Média da turma: {media:.2f}")
print(f"Maior nota: {maior_nota:.2f}")
print(f"Menor nota: {menor_nota:.2f}")
print("-" * 30)
print("Lista completa das notas:")
for idx, nota in enumerate(notas, start=1):
    print(f"Aluno {idx:02d}: {nota:.2f}")
