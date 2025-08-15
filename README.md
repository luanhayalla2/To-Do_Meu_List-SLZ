#To-Do_Meu_List-SLZ

Um aplicativo de lista de tarefas (To-Do_Meu_List-SLZ) desenvolvido com o framework Django, que permite aos usuários gerenciar suas tarefas de forma eficiente.

## Funcionalidades Principais

*   **Autenticação de Usuários:**
    *   Cadastro de novos usuários.
    *   Login e Logout seguros.
    *   Páginas de autenticação com design moderno.
*   **Gerenciamento de Tarefas:**
    *   Criar, visualizar, editar e excluir tarefas.
    *   Marcar tarefas como concluídas.
    *   As tarefas são privadas e associadas a cada usuário.
*   **Design e Experiência do Usuário:**
    *   Interface moderna e responsiva, utilizando Bootstrap 5.
    *   **Modo Noturno (Dark Mode):** Botão para alternar facilmente entre o tema claro e escuro.
    *   Layout aprimorado para uma melhor experiência de usuário em todas as páginas (Login, Cadastro, Lista de Tarefas).
    *   Responsividade aprimorada para dispositivos móveis.

## Tecnologias Utilizadas

*   **Backend:** Python, Django
*   **Frontend:** HTML, CSS, Bootstrap, JavaScript
*   **Banco de Dados:** SQLite (padrão do Django para desenvolvimento)

## Pré-requisitos

*   Python 3.x
*   Pip (gerenciador de pacotes do Python)

## Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/luanhayalla2/DJANGO.git
    cd DJANGO
    ```

2.  **Crie e ative um ambiente virtual:**

    *No Windows:*
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    *No macOS/Linux:*
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install Django
    ```
    *(**Nota:** Para um melhor gerenciamento de dependências, você pode criar um arquivo `requirements.txt` com o comando `pip freeze > requirements.txt` e depois instalar com `pip install -r requirements.txt`)*

4.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário para acessar o admin do Django (opcional):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7.  Abra seu navegador e acesse `http://127.0.0.1:8000/` para ver a aplicação.

## Contribuição

Contribuições são bem-vindas! Se você tiver alguma ideia para melhorar este projeto, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.
