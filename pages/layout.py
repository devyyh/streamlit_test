import streamlit as st

st.title("Layout")

col1, col2 = st.columns(2)

with col1:
    st.write("col1!!!")
with col2:
    st.write("col2!!!")