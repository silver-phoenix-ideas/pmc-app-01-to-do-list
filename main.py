prompt = "Type add, show, edit, complete or exit: "
todo_list = []

while True:
    user_action = input(prompt).strip().casefold()

    match user_action:
        case "add":
            todo_item = input("Enter to do item: ")
            todo_list.append(todo_item.strip().title())
        case "show":
            for index, todo_item in enumerate(todo_list, start=1):
                print(index, "-", todo_item)
        case "edit":
            index = int(input("Which item do you want to edit? ")) - 1
            todo_item = input("Enter new to do item: ")
            todo_list[index] = todo_item.strip().title()
        case "complete":
            index = int(input("Which item do you want to complete? ")) - 1
            todo_list.pop(index)
        case "exit":
            print("Bye!")
            break
        case _:
            print("Unknown command.")
