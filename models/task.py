from abc import ABC, abstractmethod

class Task(ABC):
    """Molde base para as tarefas."""
    def __init__(self, task_id, desc, comp=False):
        self.__id, self.__desc, self.__comp = task_id, desc, comp

    @property
    def id(self): return self.__id
    @property
    def desc(self): return self.__desc
    @property
    def comp(self): return self.__comp

    def mark_completed(self): self.__comp = True

    @abstractmethod
    def get_detalhes(self): pass

    def to_dict(self):
        """Prepara os dados para salvar no JSON."""
        return {"id": self.id, "desc": self.desc, "comp": self.comp, "type": self.__class__.__name__}

    @staticmethod
    def from_dict(d):
        """Recria o objeto a partir do JSON."""
        cls = TarefaPrioritaria if d["type"] == "TarefaPrioritaria" else TarefaSimples
        return cls(d["id"], d["desc"], d["comp"])

class TarefaSimples(Task):
    """Tarefa comum, sem destaque."""
    def get_detalhes(self):
        return f"{self.id:02d} | [{'X' if self.comp else ' '}] {self.desc}"

class TarefaPrioritaria(Task):
    """Tarefa urgente, impressa em maiúsculo."""
    def get_detalhes(self):
        return f"{self.id:02d} | [{'X' if self.comp else ' '}] [URGENTE] {self.desc.upper()}"