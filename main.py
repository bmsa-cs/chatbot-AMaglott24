"""
Chatbot
Author: Alexander Maglott
Period/Core: 6

"""

import os
import importlib.util

import random

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)

def main():
  
  print("Hello! I am Chadbot, a chatbot for short conversation!") 
  name=input("What is your name? ")
  print("")
  one_or_two = random.randint(1,2)
  if name == "Alex":
    print("Hello Alex! That is my creator's name!") 
  elif one_or_two == 1:
    print("Hello "+ name + "! I've never met someone with that name before!")  
  else:
    print("Hello "+ name + "! One of my best friends has that name!")

  age = int(input("Is there anything else about you I should know? Oh, how about your age? How old are you? "))
  print("")
  if age < 16: 
    print("Awesome! I miss the days when I was your age...")
  elif age >= 16 and age < 21:
    print("Well into Highschool I see. Fun times, fun times...")
  else:
    print("You are old enough to drink. Make sure to always drink responsibly and never drink and drive!")

  hru = input("Anyways, how are you today? Good, bad, meh? ")
  print("")
  if hru == "Good":
    print("I'm happy to hear that! I am doing well too.")
  elif hru == "Bad":
    print("Oh, I'm sorry. Make sure to always reach out to those around you if you need help!")
  elif hru == "Meh":
    print("I can understand that. Sometimes life is just life, nothing particularly good or bad about it.")
  else:
    print("I don't understand that emotion, but hopefully it is good!")
  shows=input("Have you been enjoying any good shows lately? If so, what show? ")
  print("")
  if shows == "The Mandalorian":
    print("That's cool, I've been enjoying that too!")
  elif shows == "no":
    print("Oh, ok. Not everyone enjoys TV shows!")
  else:
    showchoice = random.randint(1,4)
    if showchoice == 1:
      showchoice = "Wanda Vision"
    elif showchoice == 2:
      showchoice = "The Office"
    else:
      showchoice = "The Mandalorian" 
    print("Awesome! I have been enjoying " +showchoice+ " lately.")
    
if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()

  """
  Question ideas:
  Introduction:
    - What is your name?
    - What is your prefered gender?
    - What is your age?
  Discussion:
    - How are you?
    - Are there any TV Shows you have been enjoying lately?
      - Answers: "Awesome! I have been enjoying (insert show)!" or "That's cool, I've been enjoying that too!"
    - Do you have a favorite character from that show?
      - Answers: "That is a cool character." or "Its always good to like many characters."
    - What is your favorite movie?
      -"I've never seen that before.""
      Why did you like that movie?
      -"Those are some good reasons, maybe I will go and watch it" or "I probably won't watch that, it doesn't seem like my kind of movie." or "That sounds like a must see!"
  Conclusion:
    "Well, it was nice talking, (Name)! I'm going to go watch that movie." or "It was nice talking, (Name)! I have to go now though. Have a nice day!"
  """
