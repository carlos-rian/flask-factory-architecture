# flask-factory-architecture
Exemplo de arquitetura de Factory com Flask.
Crud simples da tabela de user.

Flask, SqlAlchemy e Marshmallow

### Dependências.

* Python >= 3.8: https://www.python.org/downloads/source/
* Poetry: https://python-poetry.org/docs/

### Execute o progrma.
0. Abra o terminal e navegue até a pasta do projeto, no mesmo nivel onde está o arquivo pyproject.toml.
```
cd flask-factory-architecture/
ls -l
```

1. Após ter instalado o poetry, execute o comando abaixo. Este comando irá criar e ativar a virtualenv.
```
poetry shell
```
2. Instale as dependências do projeto usando o comando abaixo.
```
poetry install
```
3. Execute o Flask em seguida acesse a url: http:localhost:5000/
```
FLASK_APP="app.main:create_app()" FLASK_ENV="development" flask run
```