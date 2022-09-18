'''
Python file to handle database operations
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///todo.db', echo=False)


class Todo(Base):
    __tablename__ = 'todo'
    id = Column('id', Integer, primary_key=True)
    msg = Column('msg', String)


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


def insert_todo(msg: str):
    '''
    Insert new todo item.
    '''
    session = Session()
    todo = Todo()
    todo.msg = msg
    try:
        session.add(todo)
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()


def retrive_todo():
    '''
    get all todo objects from db
    '''
    session = Session()
    msgs = []
    try:
        list_of_todos = session.query(Todo).all()
        return list_of_todos
    except:
        session.rollback()
    finally:
        session.close()


def update_todo(id: int, msg: str):
    '''
    Update todo text for the given id
    '''
    session = Session()
    try:
        update_todo = session.query(Todo).filter(Todo.id == id)
        # update first value in the list, since id is unique, we get 1 value
        update_todo[0].msg = msg
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()


def delete_todo(id: int):
    '''
    Delete todo from db for the given id.
    '''
    session = Session()
    try:
        session.query(Todo).filter(Todo.id == id).delete()
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()


if __name__ == '__main__':
    print(retrive_todo()[0].msg)
