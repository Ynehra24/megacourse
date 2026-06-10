import pandas as pd
import datetime
import os
current = datetime.datetime.now()
FPATH = f"/Users/yatharthnehva/megacourse/Proj1/savedtodo/Todo.csv"
PATH = "/Users/yatharthnehva/megacourse/Proj1/savedtodo"

def write_to_file(FPATH, todo):
    with open(FPATH, "w") as f:
        for ind, elem in enumerate(todo):
            f.write(f"{ind + 1}. {elem}\n")
    return

def read_from_file(FPATH):
    with open(FPATH, "r") as f:
        todo = f.readlines()
        for ind, elem in enumerate(todo):
            print(f"{ind}. {elem}")

def edit_todo_file(PATH, filename):
    filename = input("Please name the todo file which you want to edit")
    filepath_full = f"PATH/{filename}"
    if(os.path.exists(filepath_full)):
        todo = pd.read_csv(filepath_full)
        user_input = input("What do you want to edit? (add/remove/exit) ")
        match user_input:
            case "add":
                added_elem = input("Enter the item: ")
                added_elem.strip()
                todo.write_to_file(filepath_full, added_elem)
            
            case "remove":
                removed = int(input("Which element would you like to remove?"))
                todo.drop(removed, inplace = True)

            case exit:
                print("Alright, saving changes....")
                todo.close()

while True:
    todo = []
    todo_element = input("Enter an action(add/show/edit/exit): ")
    match todo_element:
        case "add":
            elem = input("Enter the item: ")
            elem.strip()
            todo.append(elem)
            write_to_file(FPATH, todo)
        case "show":
            read_from_file(FPATH)
        case "edit":
            filename = input("Please name the todo file which you want to edit: ")
            edit_todo_file(PATH, filename)
        case "exit":
            break
        case _:
            print("Error: choose an actual choice from the list please")


print("Current list ", todo)