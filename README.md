# Cotação de Criptomoeda - Django Web App

Este projeto é uma aplicação web construída com **Django** que permite consultar a cotação de criptomoedas em tempo real utilizando a API **CoinGecko**. A interface do usuário é simples e direta, desenvolvida com HTML e JavaScript, e permite que o usuário insira o nome de uma criptomoeda e obtenha sua cotação em **USD**.

## Funcionalidades

- **Consulta de Criptomoedas**: O usuário pode digitar o nome de uma criptomoeda (exemplo: Bitcoin, Ethereum) e obter a cotação atual em USD.
- **Feedback Dinâmico**: A resposta da consulta é exibida dinamicamente na página web, com mensagens de erro ou sucesso.
- **Backend Django**: O backend utiliza o Django para renderizar a página e fornecer a funcionalidade de consulta via API.
  
## Estrutura do Projeto

### Arquivos principais:

- **`index.html`**: Página principal com o formulário de consulta e exibição de resultados. Utiliza JavaScript para enviar a requisição ao servidor e exibir a resposta.
- **`apps.py`**: Configuração da aplicação Django.
- **`views.py`**: Lógica do backend que trata a requisição, consulta a API da CoinGecko e retorna a cotação em formato JSON.
- **`settings.py`**: Configurações do Django, incluindo a configuração de CORS para permitir a comunicação com outras origens (por exemplo, frontend hospedado em outra URL).
  
## Como Rodar o Projeto

### Requisitos
- Python 3.x
- Django 5.x
- Biblioteca **requests** para consultas HTTP.

### Passos para Configuração

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/cotacao_cripto.git
   ```

2. **Instale as dependências**:
   Certifique-se de que o Python está instalado, então crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # no Linux/Mac
   venv\Scripts\activate     # no Windows
   pip install -r requirements.txt
   ```

   O arquivo `requirements.txt` deve conter:
   ```
   django==5.1.5
   requests==2.28.1
   ```

3. **Configure o banco de dados**:
   O projeto usa o banco de dados SQLite por padrão. Para configurar o banco de dados, execute as migrações:
   ```bash
   python manage.py migrate
   ```

4. **Inicie o servidor**:
   Execute o servidor de desenvolvimento do Django:
   ```bash
   python manage.py runserver
   ```

   O aplicativo estará disponível em `http://127.0.0.1:8000/`.

### Como Usar

1. Abra o navegador e vá até a URL do servidor (`http://127.0.0.1:8000/`).
2. Na página inicial, insira o nome de uma criptomoeda (exemplo: `bitcoin`, `ethereum`) no campo de entrada.
3. Clique no botão **Buscar Cotação**.
4. O sistema exibirá a cotação da criptomoeda em USD, ou, em caso de erro, uma mensagem indicando o que deu errado (exemplo: criptomoeda não encontrada, erro de comunicação com a API).

### Exemplo de Uso

- Se o usuário buscar por **Bitcoin (bitcoin)**, a resposta será algo como:

```
A cotação de bitcoin é: $45000.00
```

- Se o usuário tentar consultar uma criptomoeda inexistente ou houver um erro de conexão, a resposta será uma mensagem de erro:

```
Erro ao acessar a API.
```

## Estrutura de Diretórios

```bash
cotacao_cripto/
│
├── cotacoes/               # App Django que contém as views e configuração
│   ├── templates/
│   │   └── index.html      # Página principal com o formulário e resultados
│   ├── views.py            # Lógica para consulta da cotação e retorno da resposta
│   └── apps.py             # Configuração do App
├── meu_projeto_py/         # Pasta do projeto Django
│   ├── settings.py         # Configurações do Django (CORS, DB, etc.)
│   └── urls.py             # Roteamento da aplicação
├── db.sqlite3              # Banco de dados SQLite
├── manage.py               # Script de gerenciamento do Django
└── requirements.txt        # Arquivo com as dependências
```

## Considerações

- **CORS**: O projeto inclui o middleware `corsheaders` para permitir que o frontend, caso esteja hospedado em outra origem (como uma aplicação separada), consiga fazer requisições ao backend. Certifique-se de configurar o CORS corretamente em `settings.py`:
  
  ```python
  CORS_ALLOWED_ORIGINS = [
      'https://meu-projeto.vercel.app',  # Adicione o domínio correto
      'http://localhost:3000',           # Se estiver rodando localmente
  ]
  ```

- **Segurança**: Não se esqueça de configurar adequadamente o **SECRET_KEY** e outros parâmetros de segurança antes de rodar o projeto em produção.

## Contribuindo

Contribuições são bem-vindas! Para contribuir, siga estas etapas:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/cotacao_cripto.git
   ```

2. **Crie um branch**:
   ```bash
   git checkout -b minha-nova-funcionalidade
   ```

3. **Faça suas alterações**, adicione testes e **commite** suas modificações:
   ```bash
   git commit -am "Descrição das modificações"
   ```

4. **Envie seu branch**:
   ```bash
   git push origin minha-nova-funcionalidade
   ```

5. **Abra um Pull Request** para revisão.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
