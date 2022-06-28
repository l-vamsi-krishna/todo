'''
A basic todo CLI application
Create/Update/Delete the todo text
The values are saved to sqlite3 db
'''
import database

def add_item():
    '''
    Take user input and insert into DB
    '''
    new_todo=input('Type your todo text: ')
    database.insert_item(msg= new_todo)
    print('Your input is saved!!')    

def user_int_input(prompt:str):
    '''
    Validate user input for integer
    '''
    while True:
        try:
            user_input=int(input(prompt))
        except ValueError:
            print('Invalid input, number is expected')
            continue
        else:
            break
    return user_input

def view_list():
    '''
    Display todo items
    '''
    if database.retrieve_item() == []:
        print('Your TODO list is empty, start by adding some.')
    else:
        for id,value in database.retrieve_item():
            print(f'{id}. {value}')


def update_delete_item(choice:int):
    '''
    Update or Delete todo item
    '''
    if database.retrieve_item() == []:
        print('Your TODO list is empty, start by adding some.')
    else:
        valid_input=False
        ids=[]

        for id,value in database.retrieve_item():
            ids.append(id)

        while not valid_input:
            view_list()
            todo_id=user_int_input(prompt='Enter the todo number: ')
            if todo_id not in ids:
                print('Invalid input!!')
            else:
                valid_input=True
                if choice == 3:
                    msg=input('Enter the text to be updated: ')
                    database.update_item(id= todo_id,msg=msg)
                else:
                    database.delete_item(id=todo_id)
        
        print('Your list is updated')
        view_list()

def main():
    '''
    Initial function to be executed!
    '''
    print('Welcome to TODO application!!\n')
    valid_input=False
    while not valid_input:
        print('''\tOperations avialable in TODO
        1. Add item TODO.
        2. View your TODO.
        3. Update your TODO.
        4. Delete you TODO.
        5. Exit.
        ''')
        choice=user_int_input(prompt='Enter your choice: ')
        if choice not in [1,2,3,4,5]:
            valid_input=False
            print('Invalid Choice.')
        else:
            if not database.table_exists():
                database.create_table()
            if choice == 1:
                add_item()
            elif choice == 2:
                view_list()
            elif choice in [3,4]:
                update_delete_item(choice)
            else:
                valid_input=True
                print('Good Bye!!')
                quit()

        

if __name__ == '__main__':
    main()