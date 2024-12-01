#!/bin/bash

echo "Enter Your Name"
read name
echo "Hello $name, Welcome to the Quiz Game"
echo "Let's start the Quiz"
echo "Q1. What is the capital of India?"
echo "a) Delhi"
echo "b) Mumbai"
echo "c) Kolkata"
echo "d) Chennai"
read answer1
if [ $answer1 == "a" ]; then
    echo "Correct Answer"
else
    echo "Wrong Answer"
fi

echo "Q2. Who is the Prime Minister of India?"
echo "a) Narendra Modi"
echo "b) Rahul Gandhi"
echo "c) Arvind Kejriwal"
echo "d) Mamata Banerjee"
read answer2
if [ $answer2 == "a" ]; then
    echo "Correct Answer"
else
    echo "Wrong Answer"
fi

echo "Q3. What is the currency of Japan?"
echo "a) Dollar"
echo "b) Euro"
echo "c) Yen"
echo "d) Pound"
read answer3
if [ $answer3 == "c" ]; then
    echo "Correct Answer"
else
    echo "Wrong Answer"
fi

echo "Q4. Who is the CEO of Tesla?"
echo "a) Jeff Bezos"
echo "b) Elon Musk"
echo "c) Tim Cook"
echo "d) Sundar Pichai"
read answer4
if [ $answer4 == "b" ]; then
    echo "Correct Answer"
else
    echo "Wrong Answer"
fi

echo "Q5. What is the capital of Australia?"
echo "a) Sydney"
echo "b) Melbourne"
echo "c) Canberra"
echo "d) Brisbane"
read answer5
if [ $answer5 == "c" ]; then
    echo "Correct Answer"
else
    echo "Wrong Answer"
fi
echo "Thank you for playing the Quiz Game"
echo "Goodbye!"
echo "Have a nice day!"
echo "End of the Quiz Game"
echo "Exiting the Quiz Game"
echo "Bye!"

# Output
# Enter Your Name
# Alice
# Hello Alice, Welcome to the Quiz Game
# Let's start the Quiz
# Q1. What is the capital of India?
# a) Delhi
# b) Mumbai
# c) Kolkata
# d) Chennai
# a
# Correct Answer
# Q2. Who is the Prime Minister of India?
# a) Narendra Modi
# b) Rahul Gandhi
# c) Arvind Kejriwal
# d) Mamata Banerjee
# a
# Correct Answer
# Q3. What is the currency of Japan?
# a) Dollar
# b) Euro
# c) Yen
# d) Pound
# c
# Correct Answer
# Q4. Who is the CEO of Tesla?
# a) Jeff Bezos
# b) Elon Musk
# c) Tim Cook
# d) Sundar Pichai
# b
# Correct Answer
# Q5. What is the capital of Australia?
# a) Sydney
# b) Melbourne
# c) Canberra
# d) Brisbane
# c
# Correct Answer
# Thank you for playing the Quiz Game
# Goodbye!
# Have a nice day!
# End of the Quiz Game
# Exiting the Quiz Game
# Bye!
#
# In this script, we have created a simple quiz game using bash scripting. The script asks the user five questions and checks if the answers are correct or not. If the answer is correct, it displays "Correct Answer," and if the answer is wrong, it displays "Wrong Answer." At the end of the quiz, it displays a thank you message and exits the game.



