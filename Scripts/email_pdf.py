from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from flask import make_response
import io

def gerar_pdf(email_results):
    # Criar um buffer de bytes para armazenar o PDF
    buffer = io.BytesIO()

    # Configurar o tamanho da página para paisagem (landscape)
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))

    # Definir o layout da tabela
    data = [['Remetente', 'Assunto', 'Data']]
    for result in email_results:
        # Dividir o texto do assunto para evitar que fique muito longo
        assunto = result['assunto']
        if len(assunto) > 30:  # Limite de caracteres para decidir se deve quebrar o texto
            assunto = assunto[:30] + '...'  # Limitar o tamanho do texto
        data.append([result['remetente'], assunto, result['data']])

    # Criar a tabela e aplicar estilos
    table = Table(data)
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    table.setStyle(style)

    # Adicionar a tabela ao documento PDF
    elements = [table]

    # Construir o PDF
    doc.build(elements)

    # Retornar o PDF como uma resposta HTTP
    response = make_response(buffer.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=emails.pdf'
    response.headers['Content-Type'] = 'application/pdf'

    return response
