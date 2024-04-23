# Consulta de Emails com Angular, Angular Material, Flask e API do Gmail

Este é um projeto que consiste em uma ferramenta para consulta de emails por palavras-chave, dentro do assunto, corpo do email e período de tempo. O projeto utiliza Angular para o front-end, Angular Material para os componentes de UI, Flask como servidor back-end em Python e a API do Gmail para consultas de email.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- Node.js e npm
- Angular CLI
- Python
- Flask
- Google API credentials (JSON file)

## Instalação

1. Clone o repositório do projeto:

```bash
git clone https://github.com/Dieg0Ch4ves/Projeto-Emails/
```

2. Navegue até o diretório do projeto:

```bash
cd Projeto-Emails
```

3. Instale as dependências do front-end (Angular):

```bash
npm install
```

4. Instale as dependências do back-end (Flask):

```bash
pip install -r requirements.txt
```

## Configuração das Credenciais do Google API

Antes de executar o projeto, é necessário configurar as credenciais da API do Google. Siga estas etapas:

1. Acesse a [Página de Console do Desenvolvedor do Google](https://console.developers.google.com/).
2. Crie um novo projeto ou selecione um projeto existente.
3. Ative a API do Gmail para o seu projeto.
4. Crie credenciais de API do tipo "OAuth 2.0 Client IDs".
5. Baixe o arquivo JSON das suas credenciais e renomeie para `credentials.json`.
6. Coloque o arquivo `credentials.json` na raiz do diretório do projeto.

## Uso

Para iniciar o servidor Flask, execute o seguinte comando no diretório raiz do projeto:

```bash
python server_app.py
```

Em seguida, inicie o servidor de desenvolvimento do Angular com o comando:

```bash
ng serve
```

Agora, você pode acessar a aplicação em `http://localhost:4200`.

## Funcionamento do Script Python

O script Python `consulta_emails.py` é responsável por acessar a API do Gmail e processar os emails de acordo com os critérios fornecidos. Certifique-se de configurar as credenciais do Google API antes de usar este script.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
