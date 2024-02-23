from openpyxl import Workbook
from flask import make_response
import io


def salvar_em_excel(email_results):
    # Criar um novo arquivo Excel
    wb = Workbook()
    ws = wb.active

    # Escrever os dados na planilha
    ws.append(['Remetente', 'Assunto', 'Data'])
    for result in email_results:
        ws.append([result['remetente'], result['assunto'], result['data']])

    # Salvar o arquivo Excel
    excel_data = io.BytesIO()
    wb.save(excel_data)
    excel_data.seek(0)

    # Criar uma resposta HTTP com a planilha Excel como conteúdo
    response = make_response(excel_data.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=emails.xlsx'
    response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    return response