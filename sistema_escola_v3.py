# ============================================================
#  SISTEMA ESCOLAR v3 - DESAFIO FINAL | SENAI
#  Disciplina: Desenvolvimento de Sistemas / Git e GitHub
#
#  Este arquivo é o ponto de partida do seu desafio final.
#  Você NÃO vai corrigir bugs desta vez.
#  Você vai CONSTRUIR o histórico do projeto do zero,
#  seguindo as etapas do roteiro de atividade.
# ============================================================


# ------------------------------------------------------------
# ETAPA 1 — Funções já prontas (não mexa aqui)
# Faça o commit inicial com este bloco funcionando.
# ------------------------------------------------------------

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

def dividir(a, b):
    """Retorna a divisão. Protege contra divisão por zero."""
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b


# ------------------------------------------------------------
# ETAPA 2 — Funções de aluno (você vai adicionar aqui)
# Adicione UMA função por vez e faça um commit a cada adição.
# ------------------------------------------------------------

# Adicione aqui as funções conforme o roteiro pedir:

def cadastrar_aluno(nome, turma, idade):
    aluno = {
        "nome": nome,
        "turma": turma,
        "idade": idade
    }
    return aluno

# >> FUNÇÃO 6: exibir_aluno(aluno)
# >> FUNÇÃO 7: calcular_media(notas)
# >> FUNÇÃO 8: verificar_aprovacao(media)
# >> FUNÇÃO 9: gerar_email(nome, turma)
# >> FUNÇÃO 10: relatorio_aluno(aluno)


# ------------------------------------------------------------
# ETAPA 3 — Branch de melhorias (você vai criar uma branch)
# As funções abaixo são melhorias. Adicione na branch certa!
# ------------------------------------------------------------

# >> FUNÇÃO 11: calcular_frequencia(aulas_dadas, faltas)
# >> FUNÇÃO 12: situacao_final(media, frequencia)


# ------------------------------------------------------------
# ÁREA DE TESTES — atualize conforme adiciona funções
# ------------------------------------------------------------

if __name__ == "__main__":

    # ETAPA 1 - Testes das funções base
    print("=== OPERAÇÕES BÁSICAS ===")
    print("Soma 3+5:", somar(3, 5))
    print("Subtração 10-4:", subtrair(10, 4))
    print("Multiplicação 3x7:", multiplicar(3, 7))
    print("Divisão 10/2:", dividir(10, 2))
    print("Divisão 5/0:", dividir(5, 0))

    # ETAPA 2 - Descomente conforme for adicionando as funções
    # print("\n=== CADASTRO DE ALUNO ===")
    # aluno = cadastrar_aluno("Ana Lima", "DS23", 17)
    # exibir_aluno(aluno)
    # media = calcular_media([7, 8, 9, 6])
    # print("Média:", media)
    # print("Aprovado:", verificar_aprovacao(media))
    # print("E-mail:", gerar_email("Ana Lima", "DS23"))
    # relatorio_aluno(aluno)

    # ETAPA 3 - Descomente após criar a branch de melhorias
    # print("\n=== SITUAÇÃO FINAL ===")
    # freq = calcular_frequencia(40, 6)
    # print("Frequência:", freq)
    # print("Situação:", situacao_final(media, freq))
