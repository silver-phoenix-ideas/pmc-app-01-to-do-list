# Imports
import time
import FreeSimpleGUI as fsg
import localization.texts as txt
import modules.functions as functions

# Settings
fsg.theme("DarkGrey9")
fsg.set_options(font=("Helvetica", 12))
button_size = 10
button_pad = (6, 15)
popup_duration = 1
background_color = "#36393F"

# Widgets
title = fsg.Text(txt.app_title, font=("Helvetica", 14, "bold"), p=(5, 15))
clock = fsg.Text(
    time.strftime(txt.datetime_format), key="clock", font=("Helvetica", 10)
)
todo_list_box = fsg.Listbox(
    values=functions.get_todo_list(), key="todo_list",
    enable_events=True, no_scrollbar=True, s=(50, 10)
)
todo_item_field = fsg.Input(
    key="todo_item", s=40, tooltip=txt.add_prompt
)
add_button = fsg.Button(
    tooltip=txt.add_button, key="add", s=button_size, p=button_pad,
    image_source="icons/add_359849_white.png", border_width=0,
    button_color=background_color, mouseover_colors=background_color
)
edit_button = fsg.Button(
    tooltip=txt.edit_button, key="edit", s=button_size, p=button_pad,
    image_source="icons/pencil_719496_white.png", border_width=0,
    button_color=background_color, mouseover_colors=background_color
)
complete_button = fsg.Button(
    tooltip=txt.complete_button, key="complete", s=button_size, p=button_pad,
    image_source="icons/trash-bin_3964085_white.png", border_width=0,
    button_color=background_color, mouseover_colors=background_color
)
close_button = fsg.Button(
    tooltip=txt.close_button, key="close", s=button_size, p=button_pad,
    image_source="icons/close_359577_white.png", border_width=0,
    button_color=background_color, mouseover_colors=background_color
)

# Layout
layout = [
    [title, fsg.Push(), clock, close_button],
    [todo_list_box],
    [todo_item_field, add_button, edit_button, complete_button]
]

# Window
window = fsg.Window(
    txt.app_title, layout=layout, no_titlebar=True, grab_anywhere=True
)

# Logic
while True:
    event, data = window.read(1000)

    if not window.was_closed():
        window["clock"].update(value=time.strftime(txt.datetime_format))

    match event:
        case "add":
            todo_item = data["todo_item"]

            try:
                todo_item = functions.add_todo_item(todo_item)
                window["todo_item"].update(value="")
                window["todo_list"].update(values=functions.get_todo_list())
            except ValueError as e:
                fsg.popup_quick_message(
                    txt.error_empty_string,
                    auto_close_duration=popup_duration
                )

        case "edit":
            try:
                old_item = data["todo_list"][0]
            except IndexError:
                fsg.popup_quick_message(
                    txt.error_no_selected_item,
                    auto_close_duration=popup_duration
                )
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
                fsg.popup_quick_message(
                    txt.error_no_selected_item,
                    auto_close_duration=popup_duration
                )
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
