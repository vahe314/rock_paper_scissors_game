
import streamlit as stgit 
import random

st.title("Rock-Paper-Scissors Game 🎮")

st.write("""
### How to Play:
1. Choose one of the options: Rock, Paper, or Scissors.
2. The computer will randomly select its choice.
3. See who wins!
""")

user_choice = st.radio("Select your choice:", ["Rock", "Paper", "Scissors"])

choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"

if st.button("Play"):
    st.write(f"**Your choice:** {user_choice}")
    st.write(f"**Computer's choice:** {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    st.subheader(result)
