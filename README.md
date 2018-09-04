# DjangoEcommerce
Projeto de Ecommerce usando Django e Python (Udemy)

## Criar o diretório do projeto
* mkdir [nome-da-pasta]
* cd [nome-da-pasta]

## Git
### Clonar um projeto Git
* Ctrl + Shift + P
* clone
* "url do diretório"
* Escolha a pasta para o projeto
* Crie o arquivo `.gitignore` com o seguinte conteúdo:
```
# See the name for you IDE
.vscode

# If you are using sqlite3
*.sqlite3

# Name of your virtuan env
venv
*pyc

# Local settings file
local_settings.py

# Jupyter files
*.ipynb
```

## Habilitar a execução de scripts no processo atual
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

## Criar e ativar um Ambiente Virtual
* `python -m venv [nome-do-ambiente-virtual]` : _python -m venv venv_
* `.\venv\Scripts\activate`

## Atualizando o pip
python -m pip install --upgrade pip

## Instalando o PyLint
* pip install pylint-django
* Adicione nas configurações de usuário do VSCode
```
"python.linting.pylintArgs": [
    "--load-plugins=pylint_django"
],
```

## Instalando o Django
pip install django

### Criar o projeto Django
`django-admin startproject [nome-do-projeto] .`
_O ponto no final da linha é para impedir a criação de uma subpasta com o nome do projeto_

### Comandos em manage.py
* `python manage.py createsuperuser` : para criar um super usuário

* `python manage.py startapp [nome-do-app]` : criar uma app
_.\manage.py startapp core_

* `python manage.py makemigrations` : identifica as alterações a serem feitas no banco
* `python manage.py migrate` : realiza estas alterações
* `python manage.py runserver` : executa o servidor da aplicação

*******

# Fazendo deploy no Heroku
**[*Heroku*](https://www.heroku.com)**
**[*Django-Heroku*](https://github.com/gpzim98/django-heroku)**

## Escondendo algumas configurações
* pip install python-decouple
* Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
- `SECRET_KEY=[Your-Secret-Key-Here]`
_Pegue a SECRET_KEY do arquivo settings.py_
- `DEBUG=False`

### Settings.py
* from decouple import config
* SECRET_KEY = config('SECRET_KEY')
* DEBUG = config('DEBUG', default=False, cast=bool)

## Configurando o Banco de Dados
* pip install dj-database-url

### Settings.py
* from dj_database_url import parse as dburl

- default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
- DATABASES = {'default': config('DATABASE_URL', default=default_dburl, cast=dburl),}

## Arquivos Estáticos
pip install dj-static

### wsgi
* from dj_static import Cling
* application = Cling(get_wsgi_application())

### Settings.py
* STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

* STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

## Crie na raiz do projeto
1. requirements-dev.txt
* pip freeze > requirements-dev.txt

2. requirements.txt
* -r requirements-dev.txt
* gunicorn
* psycopg2

3. Procfile
* web: gunicorn [nome-da-app].wsgi --log-file -
_nome da app da url padrão '/'_

4. runtime.txt
* python-3.7.0

## Criando o app no Heroku
* **[Instale o *Heroku CLI*](https://devcenter.heroku.com/articles/heroku-cli)**
* heroku apps:create [app-name]
_Nesta etapa, lembre-se de pegar o endereço da aplicação!_

## Configure o ALLOWED_HOSTS
Inclua o endereço do seu app do Heroku na variável *ALLOWED_HOSTS* no arquivo *settings.py*
Inclua *apenas o domínio*. Retire a parte do _protocolo_ e as _barras_

## Instale o plugin de configuração do Heroku
* heroku plugins:install heroku-config

### Enviando o arquivo `.env` para o Heroku
_Você deve estar dentro da pasta onde o arquivo *.env* está_
* heroku config:push

### Para ver as configurações do Heroku
* heroku config

## Publicando a aplicação no Heroku
* git add .
* git commit -m 'Configuring the app'
* git push heroku master --force

## Criando o Banco de Dados
* heroku run python manage.py migrate

## Criando o usuário admin do Django
* heroku run python manage.py createsuperuser

*******

# Utilizando Variáveis de Ambiente

## settings.py
`SECRET_KEY = os.getenv('SECRET_KEY', '[default-value]')`

*******

# Testes

## Com o arquivo tests do Django
### Criar pasta de Teste
* Criar a pasta `tests` dentro de cada aplicação a ser testada
* Criar o arquivo `__init.py__`
* Criar os arquivos de teste `test_[o-que-testar].py`
_test_views.py_

* Delete o arquivo tests.py da pasta da aplicação

### Executando os Testes
.\manage.py test

## Com o **[Model Mommy](model-mommy.readthedocs.io)**
Para ajudar no teste de models e views

### Instalando
`pip install model_mommy`

### Executando os Testes
.\manage.py test [nome-da-app]

*******

# Lembretes!

## Você pode precisar de desabilitar o _collectstatic_
* heroku config:set DISABLE_COLLECTSTATIC=1

## Alterando uma configuração específica
* heroku config:set DEBUG=True

## Formulários

### Ferramenta para trabalhar com formulário Bootstrap/Django
`pip install django-bootstrap-form`

### Outra ferramenta para trabalar com formulários
`pip install django-widget-tweaks`

## CRUD
* Create
* Read
* Update
* Delete

## Caminho das requests
* URL
* View
    Models
    Response()

Para acessar alguma view, ela deve ser mapeada no urls.py

## Comandos Git
* `git remote -v` : para verificar os repositórios remotos atuais
* `git remote add [nome] [url]` : para adicionar um repositório remoto
* `git push [nome-remote] [branch]` : fazer um pushing para o remote/branch
* `git remote show _[nome-remote]_` : inspecionar um repositório

## Instalando o iPython
Um console python melhorado. Ferramenta que facilita a utilização do shell.
`pip install ipython`
`.\manage.py shell`

### Novo iPython
O ipython se tornou o Jupyter
`pip install jupyter`
```
jupyter notebook
```

## Painel do Admin

### Adicionando a Tabela
* Em admin.py
```
from .models import [nome-do-model]
admin.site.registr([nome-do-model]
```

### Alterando o nome da Aplicação
* Em apps.py, na class [nome-da-app]Config
`verbose_name = '[nome-desejado]'`
* Em __init__.py
`default_app_config = '[nome-da-app].apps.[nome-da-app]Config'`

## Templates
Quando é necessário que uma variável esteja disponivel em todos os templates, devemos fazer o seguinte:
1. Dentro da pasta da aplicação, criar o arquivo context_processors.py
2. Neste arquivo, insira o seguinte código
```
from .models import [nome-da-tabela]

def [nome-da-variavel](request):
    return {
        '[nome-da-variavel]' : [nome-da-tabela].objects.all()
    }
```
3. Em settings.py, TEMPLATES, OPTIONS, context_processors, adicione o caminho da função criada:
```
# apps
'[nome-da-app].context_processors.[nome-da-função]',
```

## Chamando URL por Categoria
* Após criar o método get_absolute_url dentro do models.py
```
<a class="dropdown-item" href="{% url 'catalog:category' slug=category.slug %}">{{ category }}</a>

<a class="dropdown-item" href="{{ category.get_absolute_url }}">{{ category }}</a>
```

## Criando um arquivo de configurações locais
### Em .gitignore
Adicione o arquivo 'local_settings.py'

### Crie o arquivo
Na pasta raiz do projeto, crie o arquivo `local_settings.py`, com o seguinte conteúdo:
```
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### Em settings.py
No final do arquivo, adicione:
```
try:
    from local_settings import *
except ImportError:
    pass
```

### Arquivo local_settings no remote
Após configurar o arquivo `local_settings.py`, crie uma copia do mesmo e salve como `local_settings_example.py`.
Este será mandado para o repositório remoto e servirá de exemplo para outros desenvolvedores do projeto.

## Enviando emails

### Alterações no arquivo settings.py
```
# E-mail
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'admin@[nome-do-projeto].com'
```
