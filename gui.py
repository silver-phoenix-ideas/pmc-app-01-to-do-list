# Imports
import time
import FreeSimpleGUI as fsg
import localization.texts as txt
import modules.functions as functions

# Widgets
clock = fsg.Text(time.strftime(txt.datetime_format), key="clock")
label = fsg.Text(txt.add_prompt)
input_field = fsg.Input(key="todo_item")
add_button = fsg.Button(txt.add_button, key="add")
todo_list_box = fsg.Listbox(
    values=functions.get_todo_list(), key="todo_list",
    enable_events=True, size=(45, 10)
)
edit_button = fsg.Button(txt.edit_button, key="edit")
complete_button = fsg.Button(txt.complete_button, key="complete")
close_button = fsg.Button(txt.close_button, key="close")

# Layout
layout = [
    [clock],
    [label],
    [input_field, add_button],
    [todo_list_box, edit_button, complete_button],
    [close_button]
]

# Window
window = fsg.Window(txt.app_title, layout=layout, font=("Helvetica", 12))

# Logic
while True:
    event, data = window.read(1000)

    window["clock"].update(value=time.strftime(txt.datetime_format))

    match event:
        case "add":
            todo_item = data["todo_item"]

            try:
                todo_item = functions.add_todo_item(todo_item)
                window["todo_item"].update(value="")
                window["todo_list"].update(values=functions.get_todo_list())
            except ValueError as e:
                fsg.popup_quick_message(txt.error_empty_string)

        case "edit":
            try:
                old_item = data["todo_list"][0]
            except IndexError:
                fsg.popup_quick_message(txt.error_no_selected_item)
                continue

            new_item = data["todo_item"]

            todo_list = functions.get_todo_list()
            index = todo_list.index(old_item)

            try:
                functions.edit_todo_item(index, new_item)
            except ValueError as e:
                pass

            window["todo_item"].update(value="")
            window["todo_list"].update(values=functions.get_todo_list())

        case "complete":
            try:
                todo_item = data["todo_list"][0]
            except IndexError:
                fsg.popup_quick_message(txt.error_no_selected_item)
                continue

            todo_list = functions.get_todo_list()
            todo_list.remove(todo_item)
            functions.save_todo_list(todo_list)
            window["todo_item"].update(value="")
            window["todo_list"].update(values=todo_list)

        case "todo_list":
            window["todo_item"].update(value=data["todo_list"][0])

        case "close" | fsg.WINDOW_CLOSED:
            break

window.close()
