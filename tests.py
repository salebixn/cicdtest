import sys
import requests


def test_root():
    return requests.get('http://127.0.0.1/').json()


def test_items(item_id: int):
    return requests.get(f'http://127.0.0.1/items/{item_id}').json()


def test_connection():
    return requests.get('http://127.0.0.1/checkconnection').json()


def test_table(table_name: str):
    return requests.get(f'http://127.0.0.1/createtable/{table_name}').json()


def test_insert(table_name: str):
    return requests.get(f'http://127.0.0.1/insertvalues/{table_name}').json()


def test_get(table_name: str):
    return requests.get(f'http://127.0.0.1/getrow/{table_name}').json()


def main():
    root = test_root() 
    if root['Hello'] == 'World':
        print(f'test_root passed')
    else:
        print(f'test_root failed')
        print(1)
        sys.exit()

    item_id: int = 10
    items = test_items(item_id)
    if items['item_id'] == item_id:
        print(f'test_items passed')
    else:
        print(f'test_items failed')
        print(1)
        sys.exit()

    connection = test_connection()
    if connection['status'] == 0:
        print(f'test_connection passed')
    elif connection['status'] == 1:
        print(f'test_connection failed')
        print(1)
        sys.exit()

    table = test_table('testtable')
    if table['status'] == 0:
        print(f'test_table passed')
    elif table['status'] == 1:
        print(f'test_table failed')
        print(1)
        sys.exit()

    insert = test_insert('testtable')
    if insert['status'] == 0:
        print(f'test_insert passed')
    elif insert['status'] == 1:
        print(f'test_insert failed')
        print(1)
        sys.exit()

    get = test_get('testtable')
    if get['status'] == 0:
        print(f'test_get passed')
    elif get['status'] == 1:
        print(f'test_get failed')
        print(1)
        sys.exit()


if __name__ == '__main__':
    main()
