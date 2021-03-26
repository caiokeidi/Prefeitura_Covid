import psycopg2
from . import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE dados (
            id SERIAL PRIMARY KEY,
            data DATE NOT NULL ,
            vacinado DECIMAL(10) NOT NULL,
            vacinado2 DECIMAL(10) NOT NULL,
            confirmado DECIMAL(10) NOT NULL,
            recuperado DECIMAL(10) NOT NULL,
            ativo DECIMAL(10) NOT NULL,
            obito DECIMAL(10) NOT NULL,
            enfermaria DECIMAL(5,2) NOT NULL,
            uti DECIMAL(5,2) NOT NULL
        )
        """,)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        
        for command in commands:
            
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
