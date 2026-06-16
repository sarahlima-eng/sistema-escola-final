# ============================================================
#  LISTA DE TAREFAS — Atividade Rápida Git | SENAI
#  Você vai construir este programa função por função,
#  fazendo um commit a cada etapa concluída.
# ============================================================


# ------------------------------------------------------------
# JÁ PRONTO — Faça o commit inicial com este código
# ------------------------------------------------------------

tarefas = []  # lista que vai guardar as tarefas

def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("\n===== LISTA DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Sair")
    print("============================")


# ------------------------------------------------------------
# VOCÊ VAI ADICIONAR AQUI — 1 função por commit
# ------------------------------------------------------------

def adicionar_tarefa(descricao):
    tarefa = {
        "descricao": descricao,
        "concluida": False
    }
    tarefas.append(tarefa)
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["concluida"] else "✗"
        print(f"{i}. [{status}] {tarefa['descricao']}")

def concluir_tarefa(numero):
    if 1 <= numero <= len(tarefas):
        tarefas[numero - 1]["concluida"] = True
    else:
        print("Tarefa inválida.") 

def contar_pendentes():
    contador = 0

    for tarefa in tarefas:
        if not tarefa["concluida"]:
            contador += 1

    return contador


# ------------------------------------------------------------
# ÁREA DE TESTES
# ------------------------------------------------------------

if __name__ == "__main__":
    exibir_menu()

    # Descomente conforme for adicionando as funções:
    # adicionar_tarefa("Estudar Git")
    # adicionar_tarefa("Fazer atividade")
    # listar_tarefas()
    # concluir_tarefa(1)
    # listar_tarefas()
    # print("Pendentes:", contar_pendentes())
