# 📘 Assignment: Algoritmos e Estruturas de Dados

## 🎯 Objective

Nesta assignment, você vai praticar pensamento algorítmico com estruturas de dados básicas em Python. Ao final, você será capaz de modelar problemas simples do dia a dia com lista, pilha e fila.

## 📝 Tasks

### 🛠️ Resolver Problemas com Listas

#### Descrição
Implemente funções que trabalhem com listas para organizar números e extrair informações úteis.

#### Requisitos
O programa concluído deve:

- Implementar `find_max_value(numbers)` para retornar o maior valor da lista sem usar `max()`
- Implementar `count_even(numbers)` para contar quantos números pares existem
- Implementar `sort_numbers(numbers)` para retornar uma nova lista ordenada em ordem crescente
- Tratar lista vazia em `find_max_value(numbers)` retornando `None`

### 🛠️ Simular Histórico com Pilha

#### Descrição
Implemente uma pilha para simular ações de desfazer em um aplicativo simples de texto.

#### Requisitos
O programa concluído deve:

- Implementar `push_action(stack, action)` para adicionar uma ação no topo
- Implementar `undo_action(stack)` para remover e retornar a última ação
- Retornar `None` em `undo_action(stack)` quando a pilha estiver vazia
- Demonstrar o uso com pelo menos 3 ações e 2 operações de desfazer

### 🛠️ Organizar Atendimento com Fila

#### Descrição
Implemente uma fila para controlar a ordem de atendimento de estudantes.

#### Requisitos
O programa concluído deve:

- Implementar `enqueue_student(queue, name)` para adicionar estudante ao fim da fila
- Implementar `dequeue_student(queue)` para remover e retornar o primeiro estudante
- Retornar `None` em `dequeue_student(queue)` quando a fila estiver vazia
- Exibir o estado da fila após cada operação principal
