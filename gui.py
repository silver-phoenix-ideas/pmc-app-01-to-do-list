# Imports
import FreeSimpleGUI as fsg
import localization.texts as txt
import modules.functions as functions

# Widgets
label = fsg.Text(txt.add_prompt)
input_field = fsg.Input(key="todo_item")
add_button = fsg.Button(txt.add_button, key="add")

# Layout
layout = [
    [label],
    [input_field, add_button]
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
            except ValueError as e:
                pass

        case fsg.WINDOW_CLOSED:
            break

window.close()
