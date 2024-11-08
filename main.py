prompt = "Type add, show, edit or exit: "
todo_list = []

while True:
    user_action = input(prompt).strip().casefold()

    match user_action:
        case "add":
            todo_item = input("Enter to do item: ")
            todo_list.append(todo_item.strip().title())
        case "show":
            for todo_item in todo_list:
                print("-", todo_item)
        case "edit":
            index = int(input("Which item do you want to edit? ")) - 1
            todo_item = input("Enter new to do item: ")
            todo_list[index] = todo_item.strip().title()
        case "exit":
            print("Bye!")
            break
        case _:
            print("Unknown command.")
