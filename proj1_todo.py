todo = []
while True:
    todo_element = input("Enter a task or done to finish: ")
    if(todo_element == "exit"):
        break
    todo.append(todo_element)

print("Today's list ", todo)