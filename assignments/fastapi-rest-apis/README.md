# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objective

Nesta atividade, você vai construir uma API REST com FastAPI para praticar criação de rotas, validação de dados com Pydantic e tratamento de erros comuns.

## 📝 Tasks

### 🛠️ Build CRUD Endpoints

#### Descrição
Crie endpoints para cadastrar, listar, buscar, atualizar e remover itens de uma coleção simples chamada `tasks`.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks` para listar todas as tarefas.
- Implementar `POST /tasks` para criar uma nova tarefa com validação de dados.
- Implementar `GET /tasks/{task_id}`, `PUT /tasks/{task_id}` e `DELETE /tasks/{task_id}`.
- Retornar status HTTP corretos (`201`, `200`, `204`, `404`).

### 🛠️ Add Validation and Error Handling

#### Descrição
Melhore a API com regras de validação e mensagens de erro claras para entradas inválidas e recursos não encontrados.

#### Requisitos
O programa concluído deve:

- Usar modelos Pydantic para validar campos como `title`, `description` e `done`.
- Bloquear criação/atualização com `title` vazio.
- Retornar erro `404` quando uma tarefa com `task_id` não existir.
- Garantir respostas em JSON consistentes para sucesso e erro.

### 🛠️ Test API Behavior

#### Descrição
Execute a aplicação localmente e valide o comportamento das rotas usando Swagger UI em `/docs` ou uma ferramenta como curl/Postman.

#### Requisitos
O programa concluído deve:

- Iniciar a aplicação sem erros usando Uvicorn.
- Demonstrar pelo menos um caso de sucesso para criação e listagem.
- Demonstrar pelo menos um caso de erro de validação.
- Demonstrar pelo menos um caso de recurso inexistente (`404`).
