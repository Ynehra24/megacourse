todo = []
while True:
    todo_element = input("Enter an action(add/show/edit/completed/exit): ")
    match todo_element:
        case "add":
            elem = input("Enter the item: ")
            elem.strip()
            todo.append(elem)
        case "show":
            for ind, elem in enumerate(todo):
                print(f"{ind + 1}. {elem}")
        case "completed":
            inp = int(input("Which task did you finish? "))
            todo.pop(inp - 1)
            print("You have completed task ", inp)
        case "edit":
            num = int(input("Which To-do iteam would you like to edit? "))
            if(num < len(todo)):
                new_item = input("Enter the new To-do item: ")
                print("Changed the task ", todo[num], "to", new_item)
                todo[num] = new_item
        case "exit":
            break
        case _:
            print("Error: choose an actual choice from the list please")

print("Remaining list ", todo)