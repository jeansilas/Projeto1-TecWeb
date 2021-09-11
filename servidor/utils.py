import json

def extract_route(request):
    extracted = request.split()[1]
    
    return extracted[1:]  

def read_file(path):
    archive = None
    path_S = str(path)


    if path_S[-3:] == ".css" or path_S[-3:] == ".txt" or path_S[-3:] == "html" or path_S[-2:] == ".js":
        with open("../"+path,'r') as file:
            archive = file.read()
            
    else:
        with open(path,"rb") as file:
            archive = file.read()

    return archive

def load_data(path):
    with open("data/"+path,"rt", encoding="utf-8") as file:

        texto =  json.loads(file.read())
    return texto

def load_template(path):
    with open ("templates/"+path,"r") as file:
        texto = file.read()
    return texto

def save_json(params,path):
    param_json = json.dumps([params])[2:]
    ancientFile = ""
    with open(path,"r") as file:
        ancientFile = file.read()
    ancientFile = ancientFile.replace("]",",{ \n")

    with open(path,"w" ) as file:
        file.truncate(0)
        file.writelines(ancientFile)
        file.writelines(param_json)
         