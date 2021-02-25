#!/usr/bin/env python
# coding: utf-8

# In[16]:


""" Created on October 14 2020

by: Karen Larios 

name of game: Alcatraz Sharkfest Swim """

"""DocString:
    A) Introduction:
    This game consists of a swimming competition to the island of Alcatraz.
    The competitor
"""

from sys import exit
import pandas as pd
from random import randint

#Fail statement when you make the wrong decision
def fail():
    print(f"""                       You've failed, but thanks for playing! \U0001F915 """)
    retry = input(prompt = "Do you want to go back and change your answers(Yes/No): ")
    retry = retry.casefold()
    if 'y' in retry:
        Competition()
    elif 'n' in retry:
        print('The End')
    else:
        fail()

def Competition():
    print(f"""
    {' ^'*40}
    """)
    print('Swimming race day \U0001F3CA')
    input('<Press enter to start race>')
    
    print(f"""
Welcome everyone to our annual swimming competition to the island of Alcatraz.
We have a very special member today named {name} that has trained so hard.
Swimmers get ready, at the end of the countdown you can start the journey, good luck to everyone!
""")
    input('<Press enter to start countdown>')
    countdown = ['3', '2', '1']
    for number in countdown:
        print(number, '...')
        input(prompt = 'Press enter')
    input(prompt = '<Press enter to jump into the water> \U0001F30A')
    
    decision_1()
    
#Starting the competition the competitor has to make its first decision
def decision_1():
    print(f"""A few minutes have passed and you see a huge rock blocking your way. What do you do?""")
    rock = input(prompt= f"""
1. Climb up the rock and then jump into the water again
2. Go around the rock even though it will take you a lot of time
3. Stay on the rock, either way you are feeling tired
""")
    rock = rock.casefold()
    
    if rock == '1' or 'climb up' in rock:
        print("You cut your feet and you start bleeding")
        part_1()
    
    elif rock == '2' or 'go around' in rock:
        print("Now you are in the last position")
        part_2()
    
    elif rock == '3' or 'stay on the rock' in rock:
        print("You give up. ")
        fail()
        
    else:
        print("Invalid Entry")
        exit(0)

def part_1():
    print(f"""
    {'^ '*40}""")
    
    print(f"""
Oh no! You are bleeding and this is attracting sharks to you!.
    
What will you do with your shark problem now?""")
    
    decision = input(prompt = f"""
1. Start screaming for help
2. Continue swimming
3. Let the sharks eat me
""")
    
    decision = decision.casefold()
    
    if decision == '1' or 'start screaming for help' in decision:
        print("Help comes to your rescue but are out of the competition.")
        fail()
        
    elif decision == '2' or 'continue swimming' in decision:
        print(f"""
Sharks are catching up to you.""")
        part_1_1()
            
    elif decision == '3' or 'let the sharks eat me' in decision:
        print("You get eaten by sharks")
        fail()
    else:
        print("Invalid Entry")
        exit(0)

def part_2():
    print(f"""The race is almost over but you start feeling tired and you want to give up.
    What would be your first thought to motivate yourself and get through the finish line?""")
    
    thought = input(prompt = f""" Write what will motivate you to continue: 
    """)
    print(f"""{thought} is a great motivation. You managed to finish the race on third place. 
    Congratulations! \U0001F949""")
    input('<Press enter to exit>')
    exit(0)
    
def part_1_1():
    print("Do you think you can escape from sharks? Faith will decide your destiny ")
    
    chances = 1
    
    while chances > 0:
        faith = randint(0, 1)
        print(f"""
What's your guess?
1. I will survive
2. Sharks will eat me
""")
        
        guess = input("> ")
        
        if "1" in guess or "i will survive" in guess:
            if faith == 0:
                print(f"""
{name}. Your faith is to survive today. You escaped from sharks!!!
All that training did you good.""")
                input('<Press enter to continue>')
                decision_2()
                break
            
            else:
                print(f"""You get eaten by sharks.""")
                
                chances -= 1
                
                
        elif "2" in guess or "sharks will eat me" in guess:
            if faith == 1:
                print(f"""
{name}. Your faith is to survive today. You escaped from sharks!!!

All that training did you good.""")
                
                input('<Press enter to continue>')
                decision_2()
                break
            
            else:
                print(f"""You get eaten by sharks.""")
                chances -= 1
    fail()


def decision_2():
    print(f"""
This race is almost over. Just a few meters left and you are trying to swim faster.
Suddenly you remember the exercises on your training schedule and you are trying to pick one
that allows you to swim faster.
""")
    print(training_schedule)
    
    exercise = input(prompt =f"""
What exercise you think is better to make you swim faster? """)
    exercise = exercise.casefold()
   
    if 'freestyle' in exercise:
        print(f"""                 
        
                          Congratulations! You won the race. Here is your 1st place trophy \U0001F3C6""")
        
    elif 'butterfly style' in exercise or 'backstroke style' in exercise or 'breaststroke style' in exercise or 'running' in exercise or 'go up and down bleachers' in exercise or 'swim around the shore' in exercise:
            print("You got very tired super quick. You drowned")
            fail()
                
    else:
        print('Invalid Entry')
        exit(0)
       

#Defining the variables used in the story
def Intro():
    global name
    global training_schedule

#Start of the story. Users can sign in to the competition
print(f"""Sign in to the annual swimming competition to the island of Alcatraz. 
We will provide to you some training exercises so that you can get ready before the competition.
To sign in you only need to fill out a simple format. """)
input('<Press enter to start>')
name = input (prompt = "What is your name? ")
age = input(prompt = "What is your age? ")
level = input(prompt = f"""Select your level of swimming expertise: 

(Please type the number or word of your choice)
1. Beginner
2. Intermediate
3. Expert 
""")
level = level.casefold() #.casefold can read any character typed

#If you type 1,2 or 3 or any of the words python can recognize and make a selection
if level in ['1', '2', '3'] or 'beginner' in level or 'intermediate' in level or 'expert' in level:
                print (f"""
Thank you for submiting your information {name}.
I recommend you to follow the next training to be ready for the competition.""")
            
else:
    print("Invalid Entry")
    exit(0)
    
    input('<Press enter to continue>')

#List created to show the exercises with their own times   
ex_1 = ['Running', '10 min']
ex_2 = ['Go up and down bleachers', '10 min']
ex_3 = ['Swim around the shore', '20 min']
ex_4 = ['Freestyle', '15 min']
ex_5 = ['Butterfly style', '10 min']
ex_6 = ['Backstroke style', '10 min']
ex_7 = ['Breaststroke style', '10 min']
    
training_schedule = [ex_1, ex_2, ex_3, ex_4, ex_5, ex_6, ex_7]
training_schedule = pd.DataFrame(training_schedule,
                                columns = ['Exercise', 'Time'])#Allows us to put a name to the columns of the list
training_schedule.set_index('Exercise', inplace = True)
print(training_schedule)

input(prompt = "<Press enter to continue> ")

Competition()

            


# In[ ]:





# In[ ]:




