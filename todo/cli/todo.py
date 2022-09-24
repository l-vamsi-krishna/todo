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
    new_todo = input('Enter your task: ')
    database.insert_todo(msg=new_todo)
    print('Your input is saved!!')


def user_int_input(prompt: str):
    '''
    Validate user input for integer
    '''
    while True:
        try:
            user_input = int(input(prompt))
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
    if database.retrive_todo() == []:
        print('Your ToDo list is empty, start by adding some.')
    else:
        for todo in database.retrive_todo():
            print(f'{todo.id}. {todo.msg}')


def update_delete_item(choice: int):
    '''
    Update or Delete todo item
    '''
    if database.retrive_todo() == []:
        print('Your ToDo list is empty, start by adding some.')
    else:
        valid_input = False
        ids = []

        for todo in database.retrive_todo():
            ids.append(todo.id)

        while not valid_input:
            view_list()
            todo_id = user_int_input(prompt='Enter the task number: ')
            if todo_id not in ids:
                print('Invalid input!!')
            else:
                valid_input = True
                if choice == 3:
                    msg = input('Enter the text to be updated: ')
                    database.update_todo(id=todo_id, msg=msg)
                else:
                    database.delete_todo(id=todo_id)

        print('Your list is updated')
        view_list()


def main():
    '''
    Initial function to be executed!
    '''
    print('Welcome to My Todo application!!\n')
    valid_input = False
    while not valid_input:
        print('''\tOperations avialable:
        1. Add task.
        2. View your tasks.
        3. Update your task.
        4. Delete you task.
        5. Exit.
        ''')
        choice = user_int_input(prompt='Enter your choice: ')
        if choice not in [1, 2, 3, 4, 5]:
            valid_input = False
            print('Invalid Choice.')
        else:
            if choice == 1:
                add_item()
            elif choice == 2:
                view_list()
            elif choice in [3, 4]:
                update_delete_item(choice)
            else:
                valid_input = True
                print('Good Bye!!')
                quit()


if __name__ == '__main__':
    main()
