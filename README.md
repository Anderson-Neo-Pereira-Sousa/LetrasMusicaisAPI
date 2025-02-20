# Letras de Músicas com Streamlit

Este projeto usa o Streamlit para criar uma aplicação que permite ao usuário buscar e exibir a letra de uma música a partir de uma API pública de letras, a API Lyrics.ovh.

## Descrição

O aplicativo permite que o usuário insira o nome de uma banda e o título de uma música. Após a pesquisa, a aplicação faz uma requisição à API Lyrics.ovh e exibe a letra correspondente (se encontrada).

## Funcionalidades

- Busca a letra de músicas por banda e nome da música.
- Exibe a letra da música ou uma mensagem de erro caso a letra não seja encontrada.
- Interface simples e interativa usando o Streamlit.

## Pré-requisitos

Antes de rodar a aplicação, você precisa ter o Python instalado na sua máquina. Também é necessário ter o Poetry para gerenciar as dependências.

### Instalar o Poetry

Se você ainda não tem o Poetry, pode instalá-lo seguindo as instruções no [site oficial](https://python-poetry.org/docs/#installation).

## Instalação

1. Clone este repositório ou baixe os arquivos:
git clone https://github.com/SEU-USUARIO/nome-do-repositorio.git

2. Instale as dependências do projeto usando o Poetry. No diretório do projeto, execute o comando:
poetry install

3. Após instalar as dependências, execute a aplicação com o seguinte comando:
poetry run streamlit run app.py
