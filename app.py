import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.stoggle import stoggle
from streamlit_extras.metric_cards import style_metric_cards
import scenes
import time
import random

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Game Design
st.set_page_config(page_title="Piggy Bank Activists", page_icon="🐷")

#-----Variables-----#

# Player Variables
if "player_name" not in st.session_state:
    st.session_state.player_name = ""
if "player_career" not in st.session_state:
    st.session_state.player_career = ""
if "player_budget" not in st.session_state:
    st.session_state.player_budget = ""
if "player_insurance" not in st.session_state:
    st.session_state.player_insurance = ""

# Metric Variables
if "expenses" not in st.session_state:
    st.session_state["expenses"] = 0
if "cash" not in st.session_state:
    st.session_state["cash"] = 0
if "debt" not in st.session_state:
    st.session_state["debt"] = 0
if "investments" not in st.session_state:
    st.session_state["investments"] = 0

# Scene Variables
if "place" not in st.session_state:
    st.session_state["place"] = "introScene"
if "counter" not in st.session_state:
    st.session_state["counter"] = 0


local_css("style.css")

# Create Start Screen
st.title("🐷 Piggy Bank Activists")
start_image = st.empty()
start_image.image("images/introscene.png")
start_page_1 = st.empty()
start_page_2 = st.empty()
start_page_3 = st.empty()
start_page_1.markdown("**Welcome to Piggy Bank Activists!** Get ready to embark on a uniquely Singaporean journey where every financial decision you make will shape your destiny.")
start_page_2.markdown("From the bustling streets of Orchard Road to the peaceful parks of Bishan, Singapore is yours to explore. Along the way, you'll face important decisions—whether it's saving for a big goal, choosing the right investment, or managing your spending wisely.")
start_page_3.markdown("But be careful! Just like in real life, challenges and surprises await at every turn. Are you ready to make smart choices and build your financial future? Let’s get started on this adventure!")
st.divider()

col1, col2 = st.columns([1, 2])
with col1:
    player_name_container = st.empty()
    player_name = player_name_container.text_input("Input your name: ")

with col2:
    player_career_container = st.empty()
    player_career = player_career_container.radio(
        "Choose your career:",
        ["Doctor", "Technician", "Teacher"],
        help="Each career has different starting conditions and earning potential. Choose wisely!",
        captions=["👩‍⚕️ Begin with +300 debt. Credit +100 Salary each round", "🧑‍🔧 Begin with +0 debt. Credit +30 Salary each round", "🧑‍🏫 Begin with +75 debt. Credit +50 Salary each round"],
    )

enter_button_container = st.empty()
enter_button = enter_button_container.button("Start your adventure!")

if enter_button:
    if player_name.strip() != "":
        st.session_state.player_name = player_name
        st.session_state.player_career = player_career
        start_image.empty()
        player_name_container.empty()
        enter_button_container.empty()
        player_career_container.empty()
    else:
        st.warning("Please enter your name before proceeding.")


# START THE GAME
if st.session_state.player_name != "":

    # Delete Start Screen
    start_page_1.empty()
    start_page_2.empty()
    start_page_3.empty()
    start_image.empty()
    player_career_container.empty()
    player_name_container.empty()
    enter_button_container.empty()

    if st.session_state.place == "introScene":
        scenes.introScene()
    elif st.session_state.place == "insuranceScene":
        scenes.insuranceScene()
    elif st.session_state.place == "bonusScene":
        scenes.bonusScene()
    elif st.session_state.place == "houseScene":
        scenes.houseScene()
    elif st.session_state.place == "unexpectScene":
        scenes.unexpectScene()
    elif st.session_state.place == "endScene":
        scenes.endScene()

        # Salary budget per round
    if st.session_state["counter"] > 0:
        st.session_state["investments"] += st.session_state["investments"] * 0.1
        if st.session_state.player_career == "Doctor":
            if st.session_state.player_budget == 1:
                st.session_state["cash"] += 30
                st.session_state["expenses"] += 70
            elif st.session_state.player_budget == 2:
                st.session_state["cash"] += 30
                st.session_state["expenses"] += 65
                st.session_state["investments"] += 15
            elif st.session_state.player_budget == 3:
                st.session_state["cash"] += 30
                st.session_state["expenses"] += 50
                st.session_state["investments"] += 30

        elif st.session_state.player_career == "Technician":
            if st.session_state.player_budget == 1:
                st.session_state["cash"] += 30
                st.session_state["expenses"] += 70
            elif st.session_state.player_budget == 2:
                st.session_state["cash"] += 30
                st.session_state["expenses"] += 65
                st.session_state["investments"] += 15
            elif st.session_state.player_budget == 3:
                st.session_state["cash"] += 30
                st.session_state["expenses"] += 50
                st.session_state["investments"] += 30

        elif st.session_state.player_career == "Teacher":
            if st.session_state.player_budget == 1:
                st.session_state["cash"] += 30
                st.session_state["expenses"] += 70
            elif st.session_state.player_budget == 2:
                st.session_state["cash"] += 30
                st.session_state["expenses"] += 65
                st.session_state["investments"] += 15
            elif st.session_state.player_budget == 3:
                st.session_state["cash"] += 30
                st.session_state["expenses"] += 50
                st.session_state["investments"] += 30

    # player stats
    col1, col2, col3, col4  = st.columns(4)
    col1.metric(label="Expenses", value=st.session_state.expenses)
    col2.metric(label="Cash", value=st.session_state.cash)
    col3.metric(label="Debt", value=st.session_state.debt)
    col4.metric(label="Investment", value=st.session_state.investments)
    style_metric_cards(
        background_color="#21212f", border_color="#5b488b", border_left_color="#5b488b"
    )

