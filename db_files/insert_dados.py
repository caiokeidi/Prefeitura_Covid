import psycopg2
from . import config

def insert_dados(data):
    commands = (
        f"""
        INSERT INTO dados(
        DATA, 
        VACINADO, 
        VACINADO2, 
        CONFIRMADO,
        RECUPERADO, 
        ATIVO, 
        OBITO, 
        ENFERMARIA, 
        UTI) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s
    )
        """,)
    conn = None
    try:
        
        params = config()
        
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        for command in commands:
            cur.execute(command, (data['data'], 
        data['vacinado'], 
        data['vacinado2'], 
        data['confirmado'], 
        data['recuperado'], 
        data['ativo'],
        data['obito'],
        data['enfermaria'],
        data['uti']))
        
        cur.close()
        
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    insert_dados()
