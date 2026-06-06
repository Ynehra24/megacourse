todo = []
while True:
    todo_element = input("Enter an action(add/show/completed/exit): ")
    match todo_element:
        case "add":
            elem = input("Enter the item: ")
            todo.append(elem)
        case "show":
            print(todo)
        case "completed":
            inp = input("Which task did you finish? ")
            if inp in todo:
                todo.remove(inp)
                print("You have completed task ", inp)
            else:
                print("Error: Task not found")

        case "exit":
            break

print("Remaining list ", todo)