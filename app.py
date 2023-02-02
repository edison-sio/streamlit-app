import streamlit as st

st.title('Streamlit app')

if 'disable_input' not in st.session_state:
    st.session_state.disable_input = False
if 'disable_input_button' not in st.session_state:
    st.session_state.disable_input_button = 'Disable'

def button_click():
    st.session_state.disable_input = not st.session_state.disable_input
    if st.session_state.disable_input:
        st.session_state.disable_input_button = 'Enable'
    else:
        st.session_state.disable_input_button = 'Disable'

st.button(label=st.session_state.disable_input_button, on_click=button_click)
st.text_input(label='Input', disabled=st.session_state.disable_input)