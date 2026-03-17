from processamento import analisar_alunos

alunos = [
    ("Beatriz", [9, 8, 10, 9]),     # Aluna de alta performance
    ("Ricardo", [4, 5, 3]),         # Notas baixas para testar "Performance Crítica"
    ("Fernanda", [7, 7, 8]),        # Notas estáveis
    ("Bruno", [2]),                 # Apenas uma nota (testar cálculo de média)
    ("Clara", [10, 10]),            # Notas máximas
    ("Marcos", [0, 0, 0]),          # Notas zeradas (diferente de lista vazia)
    ("Daniela", [6, 8, 5, 7, 9]),   # Lista maior de notas
    ("Tiago", []),                  # Lista vazia (importante para testar erro de divisão por zero)
    ("Patrícia", [8.5, 9.2, 7.8]),  # Notas com casas decimais (float)
    ("Lucas", [5, 6]),               # Notas próximas da média
    ("Jessica", [10, 10])
]

analisar_alunos(alunos)     