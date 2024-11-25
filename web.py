# Imports
import time
import streamlit as st
import localization.texts as txt
import modules.functions as functions


# Logic
def add_todo_item():
    todo_item = st.session_state["todo_item"]

    try:
        functions.add_todo_item(todo_item)
    except ValueError as e:
        st.session_state["error"] = txt.error_empty_string

    st.session_state["todo_item"] = ""


def main():
    todo_list = functions.get_todo_list()

    st.title(txt.app_title)
    st.subheader(time.strftime(txt.date_format))

    for index, todo_item in enumerate(todo_list):
        if st.checkbox(todo_item):
            functions.remove_todo_item(index)
            st.rerun()

    st.text_input(
        label=txt.add_prompt, label_visibility="hidden",
        placeholder=txt.add_placeholder + "...",
        key="todo_item", on_change=add_todo_item
    )

    if "error" in st.session_state:
        st.error(st.session_state["error"])
        del st.session_state["error"]


main()
