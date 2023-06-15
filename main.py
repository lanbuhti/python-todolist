def get_todos(filename="todos.txt"):
    """ Read a text file and return the list of to-do items. """
    with open(filename, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filename="todos.txt"):
    """ Write the to-do items list in a text file. """
    with open(filename, "w") as file:
        file.writelines(todos_arg)


while True:
    user_input = input("Type add, show, edit, complete or exit: ").strip()

    if user_input.startswith("add "):
        todo = user_input[4:] + "\n"
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)

    elif user_input.startswith("show"):
        todos = get_todos()
        todos = [item.strip("\n") for item in todos]
        for index, todo in enumerate(todos):
            row = f"{index + 1}-{todo.capitalize()}"
            print(row)

    elif user_input.startswith("edit "):
        try:
            number = int(user_input[5:])
            number = number - 1
            new_todo = input("Enter the new value: ")

            todos = get_todos()
            todos[number] = new_todo + "\n"
            write_todos(todos)
        except ValueError:
            print("Invalid command")

    elif user_input.startswith("complete "):
        try:
            number = int(user_input[9:])
            todos = get_todos()
            removed_todo = todos.pop(number - 1).strip("\n")
            write_todos(todos)
            message = f"Todo {removed_todo} was marked as completed"
            print(message)
        except IndexError:
            print("There is no value with that index")

    elif "exit" in user_input:
        break

    else:
        print(f"Unknown command: {user_input}")
print("Bye!")
