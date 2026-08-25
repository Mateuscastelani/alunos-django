# Projeto de Gerenciamento de Alunos (Django & DRF)

Este é um projeto full-stack desenvolvido em Python utilizando o framework Django e o **Django REST Framework (DRF)**. O sistema demonstra os conceitos fundamentais de arquitetura MTV (Model-Template-View) para renderização de páginas web e a construção de uma **API RESTful** para o consumo de dados em formato JSON.

O projeto foi pensado para gerenciar registros de alunos da Univesp, demonstrando as melhores práticas do backend moderno.

## 💻 Sobre o Projeto

O objetivo principal deste projeto foi construir uma aplicação web funcional capaz de persistir e exibir dados em tela. Ele foi estruturado utilizando boas práticas de componentização do Django, separando as configurações globais do aplicativo de visualização (`website`).

**Funcionalidades Implementadas:**
* Mapeamento Objeto-Relacional (ORM) para criação de tabelas via SQLite.
* Inserção de dados de alunos (Nome, Sobrenome, Matrícula) via Django Shell.
* Utilização de *Class-Based Views* (`ListView`) para otimização do código de visualização HTML.
* Renderização de dados dinâmicos utilizando a *Template Language* nativa do Django.
* **[NOVO]** Serialização de dados utilizando o `Django REST Framework`.
* **[NOVO]** Construção de Endpoints (APIViews) devolvendo dados em JSON puro.
* **[NOVO]** Configuração de rotas isoladas (`/alunos/` para interface e `/api/alunos/` para dados).
* Configuração e roteamento dinâmico de URLs.

## 🛠️ Tecnologias Utilizadas

* **Python 3.14**
* **Django 6.1**
* **Django REST Framework 3.18**
* **SQLite** (Banco de dados padrão)
* **HTML5** (Templates)

  👨‍💻 Autor
Desenvolvido por Mateus Castellani.
