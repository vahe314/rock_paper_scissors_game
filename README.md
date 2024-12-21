Using st.title we give the name of the game (in this case Rock Paper Scissors)
Then with the help of st.write we write the instuctions of the game.
After we create a selectbox named level and give the difficulties of levels (Easy, Medium, Hard)
Using st.radio users can select Rock Paper or Scissors 
Then we create function get_computer_choice in which we can create levels for the game
In easy level we give weights 0.05 that the computer will choose the same thing as you (5 percent probability that the game will be tie)
Weight 0.1 means that the computer will select the wining choice (10 percent probability that the computer will win)
Weight 0.85 means that the computer will select the losing choice (85 percent probability that the user will win) 
In medium level we do not set weight so computer will generate its choice in equal proportions
And in hard level we set the same weigth as in the easy level but there is 10 percent probaility that the user will win and 85 percent that the computer will win 
After creating this function we can give inputes of level and user's choice
Then we write another function named determine_winner and write settings in which situations how the game will end
Everything is ready so we just need to create Play button then print the choices of the user and the computer and then determine the winner

(Python version 3.12.7)
