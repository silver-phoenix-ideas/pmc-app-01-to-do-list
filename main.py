prompt = "Type add, show or exit: "
todo_list = []

while True:
    user_action = input(prompt).strip().casefold()

    match user_action:
        case "add":
            todo_item = input("Enter to do item: ")
            todo_list.append(todo_item.title())
        case "show":
            for todo_item in todo_list:
                print("-", todo_item)
        case "exit":
            print("Bye!")
            break
        case _:
            print("Unknown command.")
