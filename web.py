import streamlit as st
import localization.texts as txt
import modules.functions as functions

todo_list = functions.get_todo_list()

st.title(txt.app_title)

for todo_item in todo_list:
    st.checkbox(todo_item)

st.text_input("", placeholder=txt.add_placeholder + "...")
