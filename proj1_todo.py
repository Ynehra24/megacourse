todo = []
while True:
    todo_element = input("Enter an action(add/show/completed/exit): ")
    match todo_element:
        case "add":
            elem = input("Enter the item: ")
            elem.strip()
            todo.append(elem)
        case "show":
            for elem in todo:
                print(elem)
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