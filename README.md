# Workshop Data Quality : ETL com Pydantic e Pandera

Este projeto de Engenharia de Dados tem como objetivo assegurar a qualidade e a estrutura dos dados por meio de um processo de ETL. Os dados são extraídos de tabelas no PostgreSQL, passam por transformações e são carregados em um banco de dados DuckDB, garantindo a integridade. Além disso, o projeto conta com uma esteira de CI que executa testes unitários para validar o código, assegurando conformidade com as regras de negócio. Este workshop é conduzido pela Jornada de Dados.


## 🚀 Features

- Validação de dados com Pandera
- Operações em banco de dados com SQLAlchemy e DuckDB
- Testes automatizados com pytest
- Documentação com MkDocs

## 📋 Prerequisites

- Python 3.11 or higher
- Poetry for dependency management

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd workshop-data_quality
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Activate the virtual environment:
```bash
poetry shell
```

## 🏗️ Project Structure

```
workshop-data_quality/
├── app/            # Application source code
├── docs/           # Documentation files
├── sql/            # SQL scripts and queries
├── test/           # Test files
├── pyproject.toml  # Project configuration and dependencies
└── README.md       
```

## 🚀 Usage

- Run tests:
```bash
poetry run python app/etl.py
```

## 📚 Documentation

The project documentation is built using MkDocs and can be accessed by running:
```bash
poetry run task doc
```

This will start a local server at `http://localhost:8000` where you can view the documentation.

## 🧪 Testing

Run the test suite using:
```bash
poetry run task test
```