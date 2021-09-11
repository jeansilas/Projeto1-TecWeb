import sqlite3

class Database():

    def __init__(self,name):
        self.name = name + ".db"
        self.conn = sqlite3.connect(self.name)
        self.conn.execute(" CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY , title TEXT, details TEXT NOT NULL);")
        self.conn.commit()

    def add(self,notes):
        id = notes.id
        title = notes.title
        details = notes.details

     #    if id is None:
     #         self.conn.execute(f"INSERT INTO note (title,content) VALUES ('{title}','{content}');")
     #    elif title is None:
     #         self.conn.execute(f"INSERT INTO note (id,content) VALUES ('{id}', '{content}');")
     #    elif content is None:
     #         self.conn.execute(f"INSERT INTO note (id,title) VALUES ('{id}', '{title}');")
     #    else:
     #         self.conn.execute(f"INSERT INTO note (id, title, content) VALUES ('{id}','{title}','{content}');")
        self.conn.execute(f"INSERT INTO note  (title, details) VALUES ('{title}','{details}');")
        self.conn.commit()
    
    def get_all(self, type = "obj"):
        cursor = self.conn.execute("SELECT id,title,details FROM note;")
        lis_objs = []
        for obj in cursor:
          id = obj[0]
          title = obj[1]
          details = obj[2]
          if type == "obj":
            lis_objs.append(Note(id,title,details))
          elif type == "dict":
            lis_objs.append(dict(id=id,title=title,details=details))
        return lis_objs

    def update(self,entry):
        id = entry.id
        title = entry.title
        details = entry.details
        
        self.conn.execute(f"UPDATE note SET (title,details) = ('{title}','{details}') WHERE id = {id};")
        self.conn.commit()

    def delete(self,note_id):
        self.conn.execute(f"DELETE FROM note WHERE id={note_id}")
        self.conn.commit()


from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    details: str = ''