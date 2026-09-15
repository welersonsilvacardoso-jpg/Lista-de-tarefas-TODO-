from abc import ABC, abstractmethod

class Task(ABC):
    """Molde base para as tarefas, agora com suporte a prazos."""
    def __init__(self, task_id, desc, prazo=None, comp=False):
        self.__id, self.__desc, self.__prazo, self.__comp = task_id, desc, prazo, comp

    @property
    def id(self): return self.__id
    @property
    def desc(self): return self.__desc
    @property
    def prazo(self): return self.__prazo
    @property
    def comp(self): return self.__comp

    def mark_completed(self): self.__comp = True

    @abstractmethod
    def get_detalhes(self): pass

    def to_dict(self):
        """Prepara os dados para salvar no JSON."""
        return {"id": self.id, "desc": self.desc, "prazo": self.prazo, "comp": self.comp, "type": self.__class__.__name__}

    @staticmethod
    def from_dict(d):
        """Recria o objeto a partir do JSON."""
        cls = TarefaPrioritaria if d["type"] == "TarefaPrioritaria" else TarefaSimples
        return cls(d["id"], d["desc"], d.get("prazo"), d["comp"])

class TarefaSimples(Task):
    def get_detalhes(self):
        p_text = f" (Prazo: {self.prazo})" if self.prazo else ""
        return f"{self.id:02d} | [{'X' if self.comp else ' '}] {self.desc}{p_text}"

class TarefaPrioritaria(Task):
    def get_detalhes(self):
        p_text = f" (Prazo: {self.prazo})" if self.prazo else ""
        return f"{self.id:02d} | [{'X' if self.comp else ' '}] [URGENTE] {self.desc.upper()}{p_text}"