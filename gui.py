# Imports
import FreeSimpleGUI as fsg
import localization.texts as txt

# Layout
label = fsg.Text(txt.add_prompt)
input_field = fsg.Input()
add_button = fsg.Button(txt.add_button)

layout = [
    [label],
    [input_field, add_button]
]

window = fsg.Window(txt.app_title, layout=layout)

# Logic
window.read()
window.close()
