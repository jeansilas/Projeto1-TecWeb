import time
from utils import load_data, load_template, save_SQL,update_SQL,delete_SQL
import database
from os import error, replace
import urllib

def index(request,database):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            if chave_valor.startswith("titulo"):
                params["titulo"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")
            if chave_valor.startswith("detalhes"):
                params["detalhes"] = urllib.parse.unquote_plus(chave_valor[chave_valor.find("=")+1:], encoding="utf-8", errors="replace")    
        save_SQL(params,database)

    elif request.startswith('UPDATE'):
        request = request.replace('\r', '')  
        partes = request.split('\n\n')
        corpo = partes[1]
        note_data=corpo.split('&')
        params = {"id":note_data[0],"titulo":note_data[1],"detalhes":note_data[2]}
        update_SQL(params,database)

    elif request.startswith('DELETE'):
        request = request.replace('\r', '')  
        partes = request.split('\n\n')
        corpo = partes[1]
        delete_SQL(corpo,database)

    # O RESTO DO CÓDIGO DA FUNÇÃO index CONTINUA DAQUI PARA BAIXO...
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('note.html')

    notes_li = [
        note_template.format(title=notes['title'], details=notes['details'],id=notes['id'])
        for notes in load_data(database,"dict")
    ]
    notes = '\n'.join(notes_li)
   

    return load_template('index.html').format(notes=notes).encode()