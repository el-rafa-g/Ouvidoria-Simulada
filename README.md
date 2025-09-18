# 📣 Sistema de Gestão de Manifestações (Ouvidoria)

Este é um sistema simples de **Ouvidoria** desenvolvido em **Python** com conexão a banco de dados **MySQL**. Ele permite listar, adicionar, pesquisar, remover e editar manifestações de usuários.

## 📋 Funcionalidades

- **Listar manifestações**  
- **Adicionar uma nova manifestação**  
- **Pesquisar manifestações por termos**  
- **Remover manifestações**  
- **Editar/substituir manifestações existentes**

## 🛠️ Tecnologias utilizadas

- Python 3.x
- MySQL
- Biblioteca `mysql.connector` (via `operacoesbd.py`)

## 🔌 Conexão com o banco de dados

A conexão é feita com os seguintes parâmetros:

```python
conn = criarConexao('127.0.0.1', 'root', 'admin', 'gestao_ouvidoria')
Certifique-se de que o banco de dados gestao_ouvidoria exista e tenha as tabelas necessárias.

🗃️ Estrutura do Projeto
main.py – Script principal com o menu interativo.

operacoesbd.py – Módulo com funções para conexão e manipulação do banco de dados.

ouvidoria.py – Módulo com as operações específicas de ouvidoria (listar, adicionar, remover, etc.).

▶️ Como executar
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
Instale as dependências (se necessário):

bash
Copiar código
pip install mysql-connector-python
Execute o script principal:

bash
Copiar código
python main.py
💾 Exemplo de tabela no MySQL
sql
Copiar código
CREATE DATABASE gestao_ouvidoria;

USE gestao_ouvidoria;

CREATE TABLE manifestacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50),
    descricao TEXT
);
✍️ Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
