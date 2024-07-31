import sys
import psycopg2
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/checkconnection")
def check_db_connect():
    try:
        conn = psycopg2.connect('postgresql://postgres:123456@db/testdb')
        conn.close()
        return {'status': 0}
    except Exception as e:
        return {'status': 1}


@app.get("/createtable/{table_name}")
def create_table(table_name: str):
    try:
        conn = psycopg2.connect('postgresql://postgres:123456@db/testdb')
        with conn:
            with conn.cursor() as cur:
                # Create table
                cur.execute(f"create table {table_name} (" \
                            "id serial primary key," \
                            "brand varchar(255)," \
                            "model varchar(255)," \
                            "year int)")

                
        conn.close()

        return {'status': 0}
    except Exception as e:
        return {'status': 1, 'exception': f'{e}'}


@app.get("/insertvalues/{table_name}")
def insert_values(table_name: str):
    try:
        conn = psycopg2.connect('postgresql://postgres:123456@db/testdb')
        with conn:
            with conn.cursor() as cur:
                # Add row
                cur.execute(f"insert into {table_name} (brand, model, year) values ('Lada', 'Niva Travel', 2024)")

        conn.close()

        return {'status': 0}
    except Exception as e:
        return {'status': 1, 'exception': f'{e}'}


@app.get("/getrow/{table_name}")
def get_row(table_name: str):
    try:
        conn = psycopg2.connect('postgresql://postgres:123456@db/testdb')
        with conn:
            with conn.cursor() as cur:
                # Get row
                cur.execute(f"select * from {table_name} where id=1")
                lada = cur.fetchone()

        conn.close()

        return {'status': 0, 'row': f'id: lada[0] brand: lada[1] model: lada[2] year: lada[3]'}
    except Exception as e:
        return {'status': 1, 'exception': f'{e}'}
