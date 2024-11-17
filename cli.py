# Imports
import time
import localization.texts as txt
import modules.functions as functions

# Logic
print("\n" + time.strftime("%A, %B %d %Y"))

try:
    todo_list = functions.get_todo_list()
    print("\n" + txt.app_title)
    functions.display_todo_list(todo_list)
except FileNotFoundError:
    todo_list = []

while True:
    print()
    user_input = input(txt.action_prompt + " ")
    user_input = user_input.strip().partition(" ")

    user_action = user_input[0].casefold()
    user_data = user_input[2]

    match user_action:
        case "add":
            todo_item = user_data if user_data else input(txt.add_prompt + " ")
            todo_item = todo_item.strip().title()

            if not todo_item:
                print(txt.error_empty_string)
                continue

            todo_list.append(todo_item)

            functions.save_todo_list(todo_list)

            print(txt.add_success.format(todo_item))

        case "show":
            if user_data:
                print(txt.error_invalid_action)
                continue

            functions.display_todo_list(todo_list)

        case "edit":
            index = user_data if user_data else input(txt.edit_prompt_index + " ")

            try:
                index = int(index) - 1
            except ValueError:
                print(txt.error_not_number.format(index))
                continue

            if index < 0 or index > len(todo_list):
                print(txt.error_not_item.format(index + 1))
                continue

            old_item = todo_list[index]
            todo_item = input(txt.edit_prompt_value + " ")
            todo_item = todo_item.strip().title()

            if not todo_item:
                print(txt.error_empty_string)
                continue

            todo_list[index] = todo_item

            new_item = todo_list[index]

            functions.save_todo_list(todo_list)

            print(txt.edit_success.format(old_item, new_item))

        case "complete":
            index = user_data if user_data else input(txt.complete_prompt + " ")

            try:
                index = int(index) - 1
            except ValueError:
                print(txt.error_not_number.format(index))
                continue

            if index < 0 or index > len(todo_list):
                print(txt.error_not_item.format(index + 1))
                continue

            todo_item = todo_list.pop(index)

            functions.save_todo_list(todo_list)

            print(txt.complete_success.format(todo_item))

        case "exit":
            if user_data:
                print(txt.error_invalid_action)
                continue

            print(txt.close)
            break

        case _:
            print(txt.error_invalid_action)
