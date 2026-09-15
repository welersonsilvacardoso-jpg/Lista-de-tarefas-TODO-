import json, os
from models.task import Task, TarefaSimples, TarefaPrioritaria

class TodoList:
    """Gerencia a lista de tarefas e o arquivo de dados."""
    def __init__(self, folder="data", file="tasks.json"):
        os.makedirs(folder, exist_ok=True)
        self.path = os.path.join(folder, file)
        self.tasks = []
        self.load()

    def add(self, desc, prazo=None, prioridade=False):
        """Adiciona uma nova tarefa."""
        nid = max([t.id for t in self.tasks] + [0]) + 1
        t = TarefaPrioritaria(nid, desc, prazo) if prioridade else TarefaSimples(nid, desc, prazo)
        self.tasks.append(t)
        self.save()
        print(f"\n[+] Tarefa '{desc}' adicionada!")

    def list_all(self, filtro="todas"):
        """Exibe as tarefas aplicando filtros de visualização."""
        filtradas = self.tasks
        if filtro == "pendentes":
            filtradas = [t for t in self.tasks if not t.comp]
        elif filtro == "concluidas":
            filtradas = [t for t in self.tasks if t.comp]

        print(f"\n--- Tarefas ({filtro.capitalize()}) ---" if filtradas else f"\n[-] Nenhuma tarefa encontrada.")
        for t in filtradas: print(t.get_detalhes())

    def complete(self, t_id):
        for t in self.tasks:
            if t.id == t_id:
                t.mark_completed()
                self.save()
                return print(f"\n[v] Tarefa {t_id} concluída!")
        print("\n[!] Não encontrada.")

    def remove(self, t_id):
        self.tasks = [t for t in self.tasks if t.id != t_id]
        self.save()
        print(f"\n[-] Tarefa {t_id} removida (se existia).")

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=2)

    def load(self):
        if os.path.exists(self.path) and os.path.getsize(self.path) > 0:
            with open(self.path, 'r', encoding='utf-8') as f:
                self.tasks = [Task.from_dict(d) for d in json.load(f)]