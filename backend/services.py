from database_config import conn

cursor = conn.cursor()

def create_user(user):
    query = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s);"
    values = (user["nome"], user["email"], user["senha"])
    cursor.execute(query, values)
    conn.commit()
    
    select_query = "SELECT * FROM usuarios WHERE email = %s;"
    select_value = (user['email'],)
    cursor.execute(select_query, select_value)
    result = cursor.fetchone()
    user_result = { "id": result[0],"email": result[1], "nome": result[2]}
    return user_result

def login():
    pass

def list_users():
    cursor.execute("SELECT * FROM usuarios;")
    rows = cursor.fetchall()

    events = []
    for row in rows:
        event = {
            'id': row[0],
            'email': row[1],
            'nome': row[2]
        }
        events.append(event)

    return events

def list_event(id):
    query = "SELECT * FROM eventos WHERE id_usuario=%s"
    value = (id,)
    cursor.execute(query, value)
    rows = cursor.fetchall()

    events = []
    for row in rows:
        event = {
            'id': row[0],
            'titulo': row[1],
            'descricao': row[2],
            'data': row[3],
            'id_usuario': row[4]
        }
        events.append(event)

    return events
def create_event(event):
    query = "INSERT INTO eventos (titulo, descricao, data, id_usuario) VALUES (%s, %s, %s, %s);"
    values = (event["titulo"], event["descricao"], event["data"], event["id_usuario"])
    cursor.execute(query, values)
    conn.commit()
    
    cursor.execute("SELECT * FROM eventos")

    rows = cursor.fetchall()

    events = []
    for row in rows:
        event = {
            'id': row[0],
            'titulo': row[1],
            'descricao': row[2],
            'data': row[3],
            'id_usuario': row[4]
        }
        events.append(event)

    return events
def delete_event(id):
    query = "DELETE FROM eventos WHERE id=%s"
    value = (id,)
    cursor.execute(query, value)
    conn.commit()
def delete_user(id):
    query = "DELETE FROM usuarios WHERE id=%s"
    value = (id,)
    cursor.execute(query, value)
    conn.commit()