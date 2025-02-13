# Gerenciador de Contatos

Este projeto é um aplicativo de gerenciamento de contatos desenvolvido em Python, utilizando conceitos de Programação Orientada a Objetos e a biblioteca Flet para a interface gráfica.

## Características

- Interface gráfica intuitiva e responsiva
- Operações CRUD (Criar, Ler, Atualizar, Deletar) para contatos
- Suporte para dois tipos de contatos: Pessoal e Profissional
- Persistência de dados em arquivo de texto usando JSON
- Implementação de conceitos de POO como Abstração, Herança e Polimorfismo

## Requisitos

- Python 3.7+
- Flet 0.26.0

## Instalação

1. Clone este repositório:
Claro! Aqui está um README bem estruturado para o seu projeto no GitHub:

```markdown
# Gerenciador de Contatos

Este projeto é um aplicativo de gerenciamento de contatos desenvolvido em Python, utilizando conceitos de Programação Orientada a Objetos e a biblioteca Flet para a interface gráfica.

## Características

- Interface gráfica intuitiva e responsiva
- Operações CRUD (Criar, Ler, Atualizar, Deletar) para contatos
- Suporte para dois tipos de contatos: Pessoal e Profissional
- Persistência de dados em arquivo de texto usando JSON
- Implementação de conceitos de POO como Abstração, Herança e Polimorfismo

## Requisitos

- Python 3.12+
- Flet 0.26.0

## Instalação

1. Clone este repositório:
```

git clone <>

```

2. Entre no diretório do projeto:
```
cd gerenciador-de-contatos

```plaintext

3. Instale as dependências:
```

pip install flet==0.26.0

```plaintext

## Uso

Para executar o aplicativo, use o seguinte comando no diretório do projeto:

```

python contact_manager_ui.py

```plaintext

## Estrutura do Projeto

O projeto consiste em dois arquivos principais:

1. `contact_manager.py`: Contém a lógica de negócios, incluindo as classes de contato e o gerenciador de contatos.
2. `contact_manager_ui.py`: Implementa a interface do usuário usando Flet.

### Classes Principais

- `Contact`: Classe abstrata base para todos os tipos de contato.
- `PersonalContact`: Representa um contato pessoal, herdando de `Contact`.
- `BusinessContact`: Representa um contato profissional, herdando de `Contact`.
- `ContactManager`: Gerencia a lista de contatos e lida com a persistência de dados.
- `ContactManagerApp`: Implementa a interface gráfica do usuário.

## Funcionalidades

- Adicionar novos contatos (pessoais ou profissionais)
- Visualizar lista de contatos
- Atualizar informações de contatos existentes
- Excluir contatos
- Dados persistentes salvos em arquivo de texto

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença