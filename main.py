# Configuration
app_title = "To Do List"
filename = "to_do_list.txt"

# Localization
txt_action_prompt = "Type add, show, edit, complete or exit:"
txt_action_error = "Unknown command."
txt_add_prompt = "Enter new item:"
txt_add_success = 'Item "{0}" has been added.'
txt_edit_prompt_index = "Which item do you want to edit?"
txt_edit_prompt_value = "Enter new text: "
txt_edit_success = 'Item "{0}" has been replaced by "{1}".'
txt_complete_prompt = "Which item do you want to complete?"
txt_complete_success = 'Item "{0}" has been removed.'
txt_exit = "To do list has been saved. Bye!"

# Logic
print("\n" + app_title)

with open(filename) as file:
    todo_list = file.read().split("\n")

for index, todo_item in enumerate(todo_list, start=1):
    print(index, "-", todo_item)

while True:
    print()
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

            print(txt_add_success.format(todo_item))

        case "show":
            if user_data:
                print(txt_action_error)
                continue

            for index, todo_item in enumerate(todo_list, start=1):
                print(index, "-", todo_item)

        case "edit":
            index = user_data if user_data else input(txt_edit_prompt_index + " ")
            index = int(index) - 1

            old_item = todo_list[index]

            todo_item = input(txt_edit_prompt_value + " ")
            todo_list[index] = todo_item.strip().title()

            new_item = todo_list[index]

            with open(filename, 'w') as file:
                file.write("\n".join(todo_list))

            print(txt_edit_success.format(old_item, new_item))

        case "complete":
            index = user_data if user_data else input(txt_complete_prompt + " ")
            index = int(index) - 1

            todo_item = todo_list.pop(index)

            with open(filename, 'w') as file:
                file.write("\n".join(todo_list))

            print(txt_complete_success.format(todo_item))

        case "exit":
            if user_data:
                print(txt_action_error)
                continue

            print(txt_exit)
            break

        case _:
            print(txt_action_error)
