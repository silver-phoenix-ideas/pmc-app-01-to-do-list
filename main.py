# Configuration
filename = "to_do_list.txt"

# Localization
txt_action_prompt = "Type add, show, edit, complete or exit:"
txt_action_error = "Unknown command."
txt_add_prompt = "Enter new item:"
txt_edit_prompt_index = "Which item do you want to edit?"
txt_edit_prompt_value = "Enter new text: "
txt_complete_prompt = "Which item do you want to complete?"
txt_complete_success = 'Item "{0}" has been removed.'
txt_exit = "Bye!"

# Logic
with open(filename) as file:
    todo_list = file.read().split("\n")

while True:
    user_input = input(txt_action_prompt + " ")
    user_input = user_input.strip().partition(" ")

    user_action = user_input[0].casefold()
    user_data = user_input[2]

    match user_action:
        case "add":
            todo_item = user_data if user_data else input(txt_add_prompt + " ")
            todo_item = todo_item.strip().title()

            todo_list.append(todo_item)

            with open(filename, 'w') as file:
                file.write("\n".join(todo_list))

        case "show":
            if user_data:
                print(txt_action_error)
                continue

            for index, todo_item in enumerate(todo_list, start=1):
                print(index, "-", todo_item)

        case "edit":
            index = user_data if user_data else input(txt_edit_prompt_index + " ")
            index = int(index) - 1

            todo_item = input(txt_edit_prompt_value + " ")
            todo_list[index] = todo_item.strip().title()

            with open(filename, 'w') as file:
                file.write("\n".join(todo_list))

        case "complete":
            index = user_data if user_data else input(txt_complete_prompt + " ")
            index = int(index) - 1

            todo_item = todo_list.pop(index)
            print(txt_complete_success.format(todo_item))

            with open(filename, 'w') as file:
                file.write("\n".join(todo_list))

        case "exit":
            if user_data:
                print(txt_action_error)
                continue

            print(txt_exit)
            break

        case _:
            print(txt_action_error)
