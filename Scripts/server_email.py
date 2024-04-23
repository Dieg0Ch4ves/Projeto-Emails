from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from email_planilha import gerar_planilha
from email_buscar import processar_email
from email_pdf import gerar_pdf

app = Flask(__name__)
CORS(app)

@app.route('/emails', methods=['GET'])
@cross_origin()
def obter_emails():
    # Obtém os parâmetros da consulta da solicitaçãos
    searchObj = request.args.to_dict()

    # Chama a função processar_email com os detalhes fornecidos na solicitação
    emails = processar_email(searchObj)
    
    # Retorna os e-mails encontrados como JSON
    return jsonify(emails)

@app.route('/emails-planilha', methods=['GET'])
@cross_origin()
def obter_emails_planilha():
    # Obtém os parâmetros da consulta da solicitaçãos
    searchObj = request.args.to_dict()

    # Chama a função processar_email com os detalhes fornecidos na solicitação
    emails = processar_email(searchObj)
    response = gerar_planilha(emails)
    print(response)
    return response

@app.route('/emails-pdf', methods=['GET'])
@cross_origin()
def obter_emails_pdf():
    # Obtém os parâmetros da consulta da solicitação
    searchObj = request.args.to_dict()

    # Chama a função processar_email com os detalhes fornecidos na solicitação
    emails = processar_email(searchObj)
    
    # Gera o PDF e retorna como uma resposta HTTP
    response = gerar_pdf(emails)
    return response

if __name__ == '__main__':
    app.run(debug=True)
