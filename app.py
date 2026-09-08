import streamlit as st

from src.screens.Home_screen import Home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen


def main():

    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    if st.session_state['login_type'] == 'teacher':
        teacher_screen()

    elif st.session_state['login_type'] == 'student':
        student_screen()

    else:
        Home_screen()


main()