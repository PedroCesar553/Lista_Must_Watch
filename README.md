Must Watch - Lista de Desejos

Este projeto e uma aplicacao web desenvolvida em Python com o framework Flask para o gerenciamento de uma lista pessoal de filmes, series, jogos e livros. O sistema permite cadastrar, visualizar, editar e excluir registros (CRUD completo).

Desenvolvido como parte da disciplina de PBE2, sob orientacao dos professores Joao Roccella e Edgard, no SENAI.
Tecnologias Utilizadas

    Python 3 e Flask (Back-end)

    SQLite (Banco de dados persistente)

    CSS3 Moderno (Interface personalizada e responsiva)

    Jinja2 (Renderizacao de templates)

Como Executar o Projeto

Siga os passos abaixo para rodar a aplicacao em sua maquina local:

1. Clonar o Repositorio

git clone <url_do_seu_repositorio>
cd Lista_Must_Watch

2. Configurar Ambiente Virtual

python -m venv .venv

Ativacao:

    Git Bash: source .venv/Scripts/activate

    Windows (PowerShell): ..venv\Scripts\Activate.ps1

3. Instalar Dependencias

pip install -r requirements.txt

4. Configuracao do Banco de Dados

    Crie uma pasta chamada data na raiz do projeto.

    Renomeie o arquivo .env.example para .env.

    Certifique-se de que a variavel DATABASE aponta para a pasta correta:
    DATABASE='./data/lista.sqlite3'

5. Iniciar a Aplicacao

flask run

Acesse no navegador: http://127.0.0.1:5000
Funcionalidades

    Cadastrar: Titulo, Tipo (obrigatorios) e Indicacao (opcional).

    Consultar: Visualizacao em cards modernos e organizados.

    Editar e Excluir: Gerenciamento total dos itens da lista.

    Banco de Dados: Persistencia de dados utilizando SQLite.

Observacao para o Versionamento

Certifique-se de que arquivos de ambiente virtual (.venv) e arquivos de banco de dados local (.sqlite3) nao sejam enviados para o repositorio remoto para manter a integridade e seguranca do codigo fonte.