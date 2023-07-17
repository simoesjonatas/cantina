# Projeto Cantina Django

Bem-vindo ao projeto Cantina Django! Este é um projeto para criar um sistema de gerenciamento de cantina escolar usando o framework Django. Com este sistema, você poderá gerenciar itens do cardápio, pedidos dos alunos, estoque e muito mais.

## Funcionalidades

O sistema Cantina Django irá possuir as seguintes funcionalidades:

1. **Categoria**: Adicionar, editar e remover categoria da cantina, como lanches, bebidas, sobremesas, etc.

2. **Produtos**: Adicionar, editar e remover produtos da cantina

3. **Pedidos**: Os alunos poderão fazer pedidos através do sistema, selecionando os itens do cardápio e a quantidade desejada.

4. **Gestão de Estoque**: Acompanhamento do estoque dos itens disponíveis na cantina, com alertas quando os níveis estiverem baixos.


## Instalação

Para instalar e executar o projeto em seu ambiente local, siga os passos abaixo:

1. Clone o repositório do GitHub:

```http
git clone https://github.com/simoesjonatas/cantina.git
```

2. Acesse o diretório do projeto:

```
cd cantina
```


3. Crie um ambiente virtual (recomendado) para isolar as dependências do projeto:

```
python -m venv venv
```

4. Ative o ambiente virtual:

   - No Windows:

   ```
   venv\Scripts\activate
    ```


    - No Linux/macOS:

    ```
   source venv/bin/activate
    ```


5. Instale as dependências do projeto:
```
pip install -r requirements.txt
```

6. Realize as migrações do banco de dados:
```
python manage.py migrate
```


7. Crie um superusuário para acessar o painel de administração:
```
python manage.py createsuperuser

```


8. Inicie o servidor de desenvolvimento:

```
python manage.py runserver

```

9. Acesse o sistema Cantina Django em seu navegador em: `http://localhost:8000/`

10. Acesse o painel de administração em: `http://localhost:8000/admin/`
