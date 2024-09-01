import streamlit as st
from streamlit_extras.stoggle import stoggle
import time
import random

###############################################
#
#               intro Scene
#
################################################


def introScene():

    # possible actions
    actions = ["Take a Job", "Up-Skill", "Buy an Investment"]

    col1, col2 = st.columns(2, gap="small")
    with col1:
        # main_image
        st.image("images/introscene.png", caption="Did you know? Singapore is one of the world's top financial hubs, with the iconic Marina Bay skyline home to over 200 banks!")
    with col2:
        # scene text
        if st.session_state["scenes_counter"]["intro_counter"] == 0:
            st.markdown(
                f"<div class='container'>Welcome, {st.session_state.player_name}! You've just stepped into an exciting world where your financial choices shape your journey. From the bustling streets of Orchard Road to the peaceful parks of Bishan, Singapore is yours to explore. Along the way, you'll face important decisions—whether it's saving for a big goal, choosing the right job, or managing your spending wisely. But be careful! Just like in real life, challenges and surprises await at every turn. Are you ready to make smart choices and build your financial future? Let’s get started on this adventure!</p></div>",
                unsafe_allow_html=True,
            )

    # Create the selectbox
    selected_action = st.selectbox("Select an action:", actions, placeholder="Choose an option", index=None, key="introSceneActions")

    # Immediately display the selected action
    st.write(f"You chose to: {selected_action}")

    # Create the button for confirmation
    if st.button("Confirm Action"):
        st.write(f"Action confirmed: {selected_action}")

   
        if selected_action == "Take a Job":
            st.session_state["scenes_counter"]["intro_counter"] += 1
            st.session_state.place = "jobScene"  # we are moving our character to other scene
            st.rerun()  # rerun is streamlit specific and rerund the app

        if selected_action == "Up-Skill":
            st.session_state["scenes_counter"]["intro_counter"] += 1
            st.session_state.place = "upskillScene"
            st.rerun()
        
        if selected_action == "Buy an Investment":
            st.session_state["scenes_counter"]["intro_counter"] += 1
            st.session_state.place = "investmentScene"
            st.rerun()

def jobScene():
    st.header("Job Scene. WIP")

def upskillScene():
    st.header("UpSkill Scene. WIP")

def jobScene():
    st.header("Investment Scene. WIP")