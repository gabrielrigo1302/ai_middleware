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

- rodar o projeto: uv run main.py ou fastapi dev main.py
- buildar o projeto: uv build;
- corrigir o projeto: uv run ruff check --fix;
- formatar o projeto: uv run ruff format;

# Referências

- uv:
    - página inicial: docs.astral.sh/uv/#scripts
    - comandos: https://docs.astral.sh/uv/reference/cli/#uv
