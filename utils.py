import streamlit as st

def clear(ss_variable):
    st.session_state["temp"] = st.session_state[ss_variable]
    st.session_state[ss_variable] = ""
    st.session_state["counter"] += 1

# before changing scene you have to clear out the temp
def temp_clear():
    st.session_state["temp"] = ""