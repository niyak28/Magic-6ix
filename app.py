import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

# streamlit app to interact with backend
st.title("Magic6ix")

# create filter items
st.header("Food")
todo_id = 