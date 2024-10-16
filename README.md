# ToDoList

Repositório do Trabalho 1 da disciplina **INF1407 | Programação para Web**

## Membros
- **Matheus S. Moreira** - 1912947
- **Victor Letichevsky** - 2020701

Desenvolvemos um site para servir como uma lista de afazeres, ajudando a organizar tarefas. O projeto foi implementado usando **HTML**, **CSS** e **Python** com o framework **Django**. O site está hospedado em uma instância da **AWS**, permitindo o acesso de qualquer lugar.

## Funcionalidades
- Cadastro de novos usuários
- Login de usuários existentes
- Adicionar novas tarefas
- Marcar tarefas como concluídas
- Excluir tarefas

## Manual do Usuário

### Caso o usuário **não tenha cadastro**:
1. Na tela inicial, clique em **Cadastre-se**.
2. Insira um **nome de usuário** (mínimo de 4 caracteres).
3. Crie uma **senha** contendo letras maiúsculas, números e símbolos para maior segurança, e repita a senha no campo apropriado. Caso tenha alguma falha na criação do usuário a página será recarregada.
4. Após o cadastro, faça o **login** com seu nome de usuário e senha.

### Caso o usuário **já tenha cadastro**:
1. Na tela inicial, insira seu **nome de usuário** e **senha** e clique em **Login**. Caso tenha alguma falha na autenticação a página será recarregada.

### Adicionar Tarefas:
1. Após o login, digite o **nome da tarefa** no campo apropriado e clique em **Adicionar**.
2. Para **marcar como concluída**, clique no checkbox ao lado da tarefa.
3. Para **apagar** uma tarefa, clique no ícone de **lixeira**.

---

Projeto hospedado na AWS para fácil acesso de qualquer dispositivo com internet.

## Observações Gerais do Projeto

Conseguimos implementar as funcionalidades de **cadastro** e **login**. Quando um **nome de usuário inválido** é inserido, um alerta é gerado corretamente, porém, essa verificação **não ocorre para senhas**, o que poderia ser melhorado. A funcionalidade de **adicionar tarefas** está funcionando como esperado, conseguimos adicionar uma tarefa, atualizar ela para concluída e apagar ela.