from controllers.todo_list import TodoList

def main():
    """Gerencia o menu do terminal."""
    todo = TodoList()
    menu = "\n1. Adicionar | 2. Listar | 3. Concluir | 4. Remover | 5. Sair\nEscolha: "
    
    while (op := input(menu)) != '5':
        try:
            if op == '1':
                desc = input("Descrição: ")
                if desc.strip(): todo.add(desc, input("Prioritária? (s/n): ").lower() == 's')
            elif op == '2': todo.list_all()
            elif op == '3': todo.complete(int(input("ID para concluir: ")))
            elif op == '4': todo.remove(int(input("ID para remover: ")))
            else: print("Opção inválida.")
        except ValueError:
            print("\n[!] Digite um valor válido.")
            
    print("\nSaindo... Até mais!")

if __name__ == "__main__":
    main()