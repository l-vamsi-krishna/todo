'''
Python file to handle database operations
'''
import sqlite3

def create_table():
    '''
    CREATE A TABLE IF DOES NOT EXISTS
    '''
    if not table_exists():
        conn = sqlite3.connect('todo.db')
        cur=conn.cursor()
        with conn:
            cur.execute('''CREATE TABLE IF NOT EXISTS TODO(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            MSG TEXT
            )
            ''')
        conn.close()

def table_exists():
    '''
    Check if table exists
    '''
    conn = sqlite3.connect('todo.db')
    cur=conn.cursor()
    listOfTables = cur.execute(
    """SELECT name FROM sqlite_master WHERE type='table'
    AND name='TODO'; """).fetchall()
    if listOfTables == []:
        conn.close()
        return False
    else:
        conn.close()
        return True


def insert_item(msg:str):
    '''
    Insert todo item to table
    '''
    conn = sqlite3.connect('todo.db')
    cur=conn.cursor()
    if not table_exists():
        create_table()
    else:
        with conn:
            cur.execute('INSERT INTO TODO VALUES (NULL,:msg)',{'msg':msg})
    conn.close()

def retrieve_item(id:int=None):
    '''
    Fetch all rows from todo table
    '''
    conn = sqlite3.connect('todo.db')
    cur=conn.cursor()
    cur.execute('SELECT id,msg FROM TODO')
    list_of_todos= cur.fetchall()
    conn.close()
    return list_of_todos

def update_item(id:int,msg:str):
    '''
    Update todo based on id
    '''
    conn = sqlite3.connect('todo.db')
    cur=conn.cursor()
    with conn:
        cur.execute('UPDATE TODO SET msg = :msg WHERE ID = :id',{'msg':msg,'id':id})
    cur=conn.cursor()
    conn.close()

def delete_item(id:int):
    '''
    Delete todo from table
    '''
    conn = sqlite3.connect('todo.db')
    cur=conn.cursor()
    with conn:
        cur.execute('DELETE FROM TODO WHERE ID = :id',{'id':id})
    cur=conn.cursor()
    conn.close()
