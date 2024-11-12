# Configuration
app_title = "To Do List"
filename = "to_do_list.txt"

# Localization
txt_action_prompt = "Type add, show, edit, complete or exit:"
txt_add_prompt = "Enter new item:"
txt_add_success = 'Item "{0}" has been added.'
txt_edit_prompt_index = "Which item do you want to edit?"
txt_edit_prompt_value = "Enter new text: "
txt_edit_success = 'Item "{0}" has been replaced by "{1}".'
txt_complete_prompt = "Which item do you want to complete?"
txt_complete_success = 'Item "{0}" has been removed.'
txt_exit = "To do list has been saved. Bye!"
txt_error_invalid_action = "Unknown command."
txt_error_empty_string = "You entered an empty string."
txt_error_not_number = 'The value "{0}" is not a number.'
txt_error_not_item = 'There\'s no item with number "{0}" in the list.'

# Logic
try:
    with open(filename) as file:
        todo_list = file.read().split("\n")

    print("\n" + app_title)

    for index, todo_item in enumerate(todo_list, start=1):
        print(index, "-", todo_item)
except FileNotFoundError:
    todo_list = []

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

            if not todo_item:
                print(txt_error_empty_string)
                continue

            todo_list.append(todo_item)

            with open(filename, 'w') as file:
                file.write("\n".join(todo_list))

            print(txt_add_success.format(todo_item))

        case "show":
            if user_data:
                print(txt_error_invalid_action)
                continue

            for index, todo_item in enumerate(todo_list, start=1):
                print(index, "-", todo_item)

        case "edit":
            index = user_data if user_data else input(txt_edit_prompt_index + " ")

            try:
                index = int(index) - 1
            except ValueError:
                print(txt_error_not_number.format(index))
                continue

            try:
                old_item = todo_list[index]
            except IndexError:
                print(txt_error_not_item.format(index + 1))
                continue

            todo_item = input(txt_edit_prompt_value + " ")
            todo_item = todo_item.strip().title()

            if not todo_item:
                print(txt_error_empty_string)
                continue

            todo_list[index] = todo_item

            new_item = todo_list[index]

            with open(filename, 'w') as file:
                file.write("\n".join(todo_list))

            print(txt_edit_success.format(old_item, new_item))

        case "complete":
            index = user_data if user_data else input(txt_complete_prompt + " ")

            try:
                index = int(index) - 1
            except ValueError:
                print(txt_error_not_number.format(index))
                continue

            try:
                todo_item = todo_list.pop(index)
            except IndexError:
                print(txt_error_not_item.format(index + 1))
                continue

            with open(filename, 'w') as file:
                file.write("\n".join(todo_list))

            print(txt_complete_success.format(todo_item))

        case "exit":
            if user_data:
                print(txt_error_invalid_action)
                continue

            print(txt_exit)
            break

        case _:
            print(txt_error_invalid_action)
