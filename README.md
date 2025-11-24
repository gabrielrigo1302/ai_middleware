# Processo para a criação do projeto

- Baixar o python: https://www.python.org/downloads
- Baixar o uv: docs.astral.sh/uv/#scripts
    - Windows: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
- Inicializar o projeto usando o uv:
    - uv init __"nome_do_projeto"__
- Baixar o fastapi[standard] usando o uv: 
    - uv add fastapi[standard]
- Baixar o ruff usando o uv;
    - uv add ruff;

# Rodando o projeto

- rodar o projeto: uvicorn main:app --reload ou fastapi dev main.py
- instalar dependências: uv run main;
- buildar o projeto: uv build;
- corrigir o projeto: uv run ruff check --fix;
- formatar o projeto: uv run ruff format;
- builder docker: docker build -t ai_middleware .;

# Arquitetura

    A arquitetura desse projeto foi concebida com base na ideia de criar uma
    aplicação capaz de se conectar com múltiplos bases de dado e aplicações que forneçam funcionalidades de IA;

    A estrutura criada serve para fazer essa conexão com o menor nível de dependência em relação às aplicações externas, dando maior flexibilidade para decisões do que e quando usar;

    Todas as camadas mensionadas a seguir tem internamente uma pasta de Classes onde vão ser definidas classes que serão utilizadas naquela camada

## Gateway

- Camada onde vai ser aplicada autenticação e autorização

## Routes

- Camada onde são criadas as rotas

## Controllers

- Camada responsável por receber e responde as requisições http

## Services

- Camada responsável por toda a regra de negócio

## Orchestrator

- Camada responsável pela orquestração do uso de IAs

### Binders

- Estruturas que vão ser responsáveis por vincular uma funcionalidade destríbuida pelo orquestrador à uma distribuidora de funcinalidade de IA. Essas estruturas foram criadas para caso queira mudar a fornecedora, não precisar desfazer todas as configurações da atual

### Providers

- Estruturas responsáveis por conexão direto com as funcionalidades de IA

# Documentação da API

A documentação da API pode ser acessada através do Swagger (http://localhost:8000/docs)

# Referências

- uv:
    - página inicial: docs.astral.sh/uv/#scripts
    - comandos: https://docs.astral.sh/uv/reference/cli/#uv
