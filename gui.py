# Imports
import FreeSimpleGUI as fsg
import localization.texts as txt
import modules.functions as functions

# Widgets
label = fsg.Text(txt.add_prompt)
input_field = fsg.Input(key="todo_item")
add_button = fsg.Button(txt.add_button, key="add")
todo_list_box = fsg.Listbox(
    values=functions.get_todo_list(), key="todo_list",
    enable_events=True, size=(45, 10)
)
edit_button = fsg.Button(txt.edit_button, key="edit")

# Layout
layout = [
    [label],
    [input_field, add_button],
    [todo_list_box, edit_button]
]

# Window
window = fsg.Window(txt.app_title, layout=layout, font=("Helvetica", 12))

# Logic
while True:
    event, data = window.read()
    print(data)
    match event:
        case "add":
            todo_item = data["todo_item"]

            try:
                todo_item = functions.add_todo_item(todo_item)
                window["todo_item"].update(value="")
                window["todo_list"].update(values=functions.get_todo_list())
            except ValueError as e:
                pass

        case "edit":
            old_item = data["todo_list"][0]
            new_item = data["todo_item"]

            todo_list = functions.get_todo_list()
            index = todo_list.index(old_item)

            try:
                functions.edit_todo_item(index, new_item)
            except ValueError as e:
                pass

            window["todo_item"].update(value="")
            window["todo_list"].update(values=functions.get_todo_list())

        case "todo_list":
            window["todo_item"].update(value=data["todo_list"][0])

        case fsg.WINDOW_CLOSED:
            break

window.close()
