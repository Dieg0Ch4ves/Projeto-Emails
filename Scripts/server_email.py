from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from email_planilha import salvar_em_excel
from email_buscar import processar_email

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
    # Retorna os e-mails encontrados como JSON
    return salvar_em_excel(emails)

if __name__ == '__main__':
    app.run(debug=True)
