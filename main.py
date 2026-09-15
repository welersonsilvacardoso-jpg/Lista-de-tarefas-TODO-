from controllers.todo_list import TodoList

def main():
    """Gerencia o menu do terminal."""
    todo = TodoList()
    menu = "\n1. Adicionar | 2. Listar | 3. Concluir | 4. Remover | 5. Sair\nEscolha: "
    
    while (op := input(menu)) != '5':
        try:
            if op == '1':
                desc = input("Descrição: ")
                if desc.strip():
                    prazo = input("Prazo (ex: 15/09/2026) ou deixe em branco: ").strip()
                    todo.add(desc, prazo if prazo else None, input("Prioritária? (s/n): ").lower() == 's')
            elif op == '2':
                f = input("Filtro (1-Todas | 2-Pendentes | 3-Concluídas): ").strip()
                tipos = {'1': 'todas', '2': 'pendentes', '3': 'concluidas'}
                todo.list_all(tipos.get(f, 'todas'))
            elif op == '3': todo.complete(int(input("ID para concluir: ")))
            elif op == '4': todo.remove(int(input("ID para remover: ")))
            else: print("Opção inválida.")
        except ValueError:
            print("\n[!] Digite um valor válido.")
            
    print("\nSaindo... Até mais!")

if __name__ == "__main__":
    main()