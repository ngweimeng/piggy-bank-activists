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

# Game Variables
if "player_name" not in st.session_state:
    st.session_state.player_name = ""
if "savings" not in st.session_state:
    st.session_state["savings"] = 10000
if "debt" not in st.session_state:
    st.session_state["debt"] = 0
if "investments" not in st.session_state:
    st.session_state["investments"] = 0
if "place" not in st.session_state:
    st.session_state["place"] = "introScene"
if "counter" not in st.session_state:
    st.session_state["counter"] = 0
if "scenes_counter" not in st.session_state:
    st.session_state["scenes_counter"] = {
        "intro_counter": 0,
    }

local_css("style.css")

# Create Start Screen
st.title("🐷 Piggy Bank Activists")
start_image = st.empty()
start_image.image("images/start.webp",width=350)
start_page = st.empty()
start_page.subheader("By Order of the Piggy Bank Activists...are you ready to embark on the greatest financial challenge of your life?💰", divider="gray")

player_name_container = st.empty()
player_name = player_name_container.text_input(
    "Input your name "
    )

enter_button_container = st.empty()
enter_button = enter_button_container.button("Enter")

if enter_button:
    if player_name.strip() != "":
        st.session_state.player_name = player_name
        start_image.empty()
        player_name_container.empty()
        enter_button_container.empty()
    else:
        st.warning("Please enter your name before proceeding.")


# START THE GAME
if st.session_state.player_name != "":

    # Delete Start Screen
    start_page.empty()
    start_image.empty()
    player_name_container.empty()
    enter_button_container.empty()

    if st.session_state.place == "introScene":
        scenes.introScene()
    elif st.session_state.place == "jobScene":
        scenes.jobScene()
    elif st.session_state.place == "upskillScene":
        scenes.upskillScene()
    elif st.session_state.place == "investmentScene":
        scenes.investmentScene()
    ### TO FILL WITH GAME SCENES ###

    # player stats

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Savings", value=st.session_state.savings, delta=0)
    col2.metric(label="Debt", value=st.session_state.debt, delta=0)
    col3.metric(label="Investments", value=st.session_state.investments, delta=0)
    style_metric_cards(
        background_color="#21212f", border_color="#5b488b", border_left_color="#5b488b"
    )
