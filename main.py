filename = "to_do_list.txt"

with open(filename) as file:
    todo_list = file.read().split("\n")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().casefold()

    match user_action:
        case "add":
            todo_item = input("Enter new item: ")
            todo_item = todo_item.strip().title()
            todo_list.append(todo_item)

            with open(filename, 'w') as file:
                file.write("\n".join(todo_list))

        case "show":
            for index, todo_item in enumerate(todo_list, start=1):
                print(index, "-", todo_item)

        case "edit":
            index = int(input("Which item do you want to edit? ")) - 1
            todo_item = input("Enter new text: ")
            todo_list[index] = todo_item.strip().title()

            with open(filename, 'w') as file:
                file.write("\n".join(todo_list))

        case "complete":
            index = int(input("Which item do you want to complete? ")) - 1
            todo_item = todo_list.pop(index)
            print(f'Item "{todo_item}" was successfully removed.')

            with open(filename, 'w') as file:
                file.write("\n".join(todo_list))

        case "exit":
            print("Bye!")
            break

        case _:
            print("Unknown command.")
