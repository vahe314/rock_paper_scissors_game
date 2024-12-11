import streamlit as st 
import random

st.title("Rock-Paper-Scissors Game")

st.write("""
### How to Play:
1. Choose one of the options: Rock, Paper, or Scissors.
2. The computer will randomly select its choice based on the selected difficulty level.
3. See who wins!
""")

level = st.selectbox("Select Difficulty Level:", ["Easy", "Medium", "Hard"])

user_choice = st.radio("Select your choice:", ["Rock", "Paper", "Scissors"])

choices = ["Rock", "Paper", "Scissors"]

def get_computer_choice(level, user_choice):
    if level == "Easy":
        if user_choice == "Rock":
            return random.choices(choices, weights=[0.1, 0.1, 0.8], k=1)[0]
        elif user_choice == "Paper":
            return random.choices(choices, weights=[0.8, 0.1, 0.1], k=1)[0]
        elif user_choice == "Scissors":
            return random.choices(choices, weights=[0.1, 0.8, 0.1], k=1)[0]
    elif level == "Medium":
        return random.choice(choices)
    elif level == "Hard":
        if user_choice == "Rock":
            return random.choices(choices, weights=[0.1, 0.8, 0.1], k=1)[0]
        elif user_choice == "Paper":
            return random.choices(choices, weights=[0.1, 0.1, 0.8], k=1)[0]
        elif user_choice == "Scissors":
            return random.choices(choices, weights=[0.8, 0.1, 0.1], k=1)[0]

computer_choice = get_computer_choice(level, user_choice)

