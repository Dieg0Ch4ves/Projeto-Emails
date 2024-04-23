from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone
import os.path
import base64
import quopri


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

    if 'periodo' in detalhes_email:
        if detalhes_email['periodo'] == '1d':
            periodo = '1d'
        elif detalhes_email['periodo'] == '2d':
            periodo = '2d'
        elif detalhes_email['periodo'] == '3d':
            periodo = '3d'
        else:
            periodo = detalhes_email['periodo']
    else:
        # Se o período não for especificado, use 1 dia por padrão
        periodo = '1d'

    # Construir a query para buscar e-mails com base no período
    query = f'newer_than:{periodo}'

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

        body = None
        if 'data' in msg['payload']['body']:
            body = msg['payload']['body']['data']
            body = base64.urlsafe_b64decode(body).decode('utf-8')
        elif 'parts' in msg['payload']:
            for part in msg['payload']['parts']:
                if part['mimeType'] == 'text/html':
                    body = part['body']['data']
                    body = base64.urlsafe_b64decode(body).decode('utf-8')
                    break
        # Verificar se o e-mail corresponde aos detalhes fornecidos
        if (detalhes_email['remetente'].lower() in sender.lower()) and \
        (detalhes_email['assunto'].lower() in subject.lower()) and \
        (detalhes_email.get('corpo') is None or (body and detalhes_email['corpo'].lower() in body.lower())):
            email_results.append({
                'remetente': sender,
                'assunto': subject,
                'data': date,
                'corpo': body
            })

    print(email_results)
    return email_results
