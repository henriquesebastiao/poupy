<h1 align="center">
    <img src="project/utils/img/bitmap.png" alt="Poupy" width="150"/><br>
</h1>

<p align="center"><strong>Manage your personal budget.</strong></p>

<p align="center">
    <a href="https://github.com/henriquesebastiao/poupy/actions/workflows/ci.yml">
        <img src="https://github.com/henriquesebastiao/poupy/actions/workflows/ci.yml/badge.svg" alt="CI status"/>
    </a>
    <a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/henriquesebastiao/poupy" > 
        <img src="https://coverage-badge.samuelcolvin.workers.dev/henriquesebastiao/poupy.svg" alt="Codecov status"/> 
    </a>
    <a href="https://github.com/henriquesebastiao/poupy/blob/main/LICENSE">
        <img alt="LICENSE" src="https://img.shields.io/github/license/henriquesebastiao/poupy"/>
    </a>
</p>

<p align="center">
    <img src="project/utils/img/screenshot.png" alt="Preview"/>
</p>

Poupy é um aplicativo web para gerenciamento de orçamento e gastos pessoais, desenvolvido com Django. Ele permite o controle financeiro completo, incluindo a gestão de contas bancárias, receitas, despesas e transferências de saldo entre contas. Com um dashboard intuitivo, o usuário pode visualizar rapidamente um resumo financeiro mensal e manter suas finanças organizadas.

## Funcionalidades

- **Adição de Contas Bancárias**: Adicione e gerencie várias contas bancárias.
- **Registro de Receitas e Despesas**: Registre suas entradas e saídas de dinheiro para melhor controle.
- **Transferência entre Contas**: Movimente saldo entre contas cadastradas.
- **Dashboard Completo:**
    - Saldo Total de todas as contas.
    - Total de Entradas e Saídas Mensais para um resumo rápido do fluxo financeiro.
    - Saldo por Conta para acompanhar a situação de cada conta individualmente.
    - Maiores Movimentações: Exibe as três maiores movimentações do mês, destacando receitas e despesas mais significativas.

Tecnologias e ferramentas usadas no projeto:

- **Python** com **Django** para o backend.
- **HTML5** e **CSS3** para o frontend.
- **PostgreSQL** para armazenamento de dados.
- **PyTest** e **Selenium** para testes unitários e funcionais.
- **Docker** para desenvolvimento em containers.
- **Ruff** para formatação de código.
- **GitHub Actions** para execução de pipelines de CI.

## Executando o projeto localmente

> [!NOTE]
> Os passos listados abaixo são baseados em sistemas Unix, podendo para variar para outros sistemas operacionais. No passa a passo é exemplificada a execução com SQLite com banco de dados, mas o projeto usa PostgreSQL e Docker para deploy.

> [!IMPORTANT]
> Para executar o projeto você deve ter o [Python](https://www.python.org/) e [Git](https://git-scm.com/) instalados em seu computador.

### Clonando o repositório

```shell
git clone https://github.com/henriquesebastiao/poupy.git && cd poupy
```

## Criando e ativando o ambiente virtual Python

É essencial a criação um ambiente virtual exclusivo para o projeto, visando evitar eventuais conflito com outros pacotes python instalados em seu computador.

```shell
python -m venv .venv
source .venv/bin/activate
```

### Atualizando o `pip` e instalando as dependências do projeto

```shell
pip install --upgrade pip
pip install -r requirements.txt
```

### Configurando as variáveis de ambiente

O projeto conta com um arquivo de modelo para a criação do `.env`, sendo assim, basta apenas duplicá-lo com o nome .env

```shell
cp .env.example .env
```

### Reunindo arquivos estáticos e criando banco de dados

O último passo antes de executar o aplicativo, é juntar todos os arquivos estáticos responsáveis por dar estilo ao aplicativo e aplicar as migrações no banco de dados.

```shell
python manage.py collectstatic
python manage.py migrate
```

### Executando o aplicativo ✨

Agora execute o seguinte comando para executar o aplicativo:

```shell
python manage.py runserver
```

Acesse o aplicativo em [http://localhost:8000](http://localhost:8000)
