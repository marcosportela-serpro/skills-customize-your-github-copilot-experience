# Código Inicial: Algoritmos e Estruturas de Dados

# Tarefa 1: Listas

def find_max_value(numbers):
    # Retorne o maior valor sem usar max().
    # Se a lista estiver vazia, retorne None.
    pass


def count_even(numbers):
    # Conte quantos números pares existem na lista.
    pass


def sort_numbers(numbers):
    # Retorne uma NOVA lista ordenada em ordem crescente.
    pass


# Tarefa 2: Pilha

def push_action(stack, action):
    # Adicione uma ação no topo da pilha.
    pass


def undo_action(stack):
    # Remova e retorne a última ação.
    # Se a pilha estiver vazia, retorne None.
    pass


# Tarefa 3: Fila

def enqueue_student(queue, name):
    # Adicione o estudante ao final da fila.
    pass


def dequeue_student(queue):
    # Remova e retorne o primeiro estudante da fila.
    # Se a fila estiver vazia, retorne None.
    pass


if __name__ == "__main__":
    # Exemplo mínimo de teste manual
    nums = [7, 2, 10, 3, 8]
    print("Maior valor:", find_max_value(nums))
    print("Quantidade de pares:", count_even(nums))
    print("Lista ordenada:", sort_numbers(nums))

    stack = []
    push_action(stack, "digitou 'Olá'")
    push_action(stack, "apagou a última palavra")
    push_action(stack, "adicionou ponto final")
    print("Desfazer:", undo_action(stack))
    print("Desfazer:", undo_action(stack))

    queue = []
    enqueue_student(queue, "Ana")
    enqueue_student(queue, "Bruno")
    enqueue_student(queue, "Caio")
    print("Atendido:", dequeue_student(queue))
    print("Fila atual:", queue)
