from database import Note
import database
import json
import time

def extract_obj_attributes(object):
    return vars(object)



def extract_route(request):
    extracted = request.split()[1]
    
    return extracted[1:]  

def read_file(path):
    archive = None
    path_S = str(path)


    if path_S[-3:] == ".css" or path_S[-3:] == ".txt" or path_S[-3:] == "html" or path_S[-2:] == ".js":
        with open("../"+path,'r', encoding="utf-8") as file:
            archive = file.read()
            
    else:
        with open(path,"rb") as file:
            archive = file.read()

    return archive

def load_data(database,type):
    
    data = database.get_all(type)
    return data

def load_template(path):
    with open ("templates/"+path,"r",encoding="utf-8") as file:
        texto = file.read()
    return texto

def save_SQL(params,database):
   title = params["titulo"]
   details = params["detalhes"]
   notes = Note(title = title, details = details)
   database.add(notes)

def update_SQL(params,database):
    id = str(params["id"])
    title = str(params["titulo"])
    details = str(params["detalhes"])
    notes = Note(id=id,title=title,details=details)
    database.update(notes)

def delete_SQL(id,database):
    database.delete(str(id))
    
   