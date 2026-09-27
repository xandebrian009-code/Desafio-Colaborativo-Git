TOTAL_ALUNOS = 30
soma_turma = 0

print("=== Sistema de Cálculo de Notas ===")

for i in range(1, TOTAL_ALUNOS + 1):
  print(f"\n--- Aluno {i} de {TOTAL_ALUNOS} ---")

  # Tratamento básico para garantir que entradas numéricas não quebrem o fluxo
  try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
  except ValueError:
    print("Valor inválido! Digite apenas números.")
    continue

  # Cálculo da média
  media = (nota1 + nota2) / 2
  soma_turma += media

  # Classificação de aprovação/reprovação
  if media >= 7.0:
    status = "Aprovado"
  elif media >= 5.0:
    status = "Recuperação"
  else:
    status = "Reprovado"

  # Exibição do relatório individual
  print(f"Média: {media:.2f} | Status: {status}")

# Relatório final geral da turma
media_geral = soma_turma / TOTAL_ALUNOS
print("\n=====================================")
print("          RELATÓRIO FINAL            ")
print("=====================================")
print(f"Média geral da turma: {media_geral:.2f}")
print("Fim do processamento.")
