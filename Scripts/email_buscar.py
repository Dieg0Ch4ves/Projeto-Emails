from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone
import os.path

def processar_email(detalhes_email):
    # Autenticar e acessar a caixa de entrada do Gmail
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    creds_file = 'token.json'
    if os.path.exists(creds_file):
        credentials = Credentials.from_authorized_user_file(creds_file, SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        credentials = flow.run_local_server()

        with open(creds_file, 'w') as token:
            token.write(credentials.to_json())

    # Configuração da API do Gmail
    service = build('gmail', 'v1', credentials=credentials)

    # Query para buscar e-mails recentes (enviados nas últimas 24 horas)
    query = 'newer_than:1d'

    # Lista de e-mails
    result = service.users().messages().list(userId='me', q=query).execute()
    messages = result.get('messages', [])

    # Lista para armazenar os resultados
    email_results = []

    # Loop através dos e-mails
    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        headers = msg['payload']['headers']
        
        # Obter o endereço do remetente
        sender = [header['value'] for header in headers if header['name'] == 'From']
        sender = sender[0] if sender else ''
        
        # Obter o assunto do e-mail
        subject = [header['value'] for header in headers if header['name'] == 'Subject']
        subject = subject[0] if subject else ''
        
        # Obter a data de envio do e-mail
        date = [header['value'] for header in headers if header['name'] == 'Date']
        date = date[0] if date else ''

        # Verificar se o e-mail corresponde aos detalhes fornecidos
        if (detalhes_email['remetente'] in sender) and (detalhes_email['assunto'] in subject):
            email_results.append({
                'remetente': sender,
                'assunto': subject,
                'data': date
            })
    print(email_results)
    return email_results
