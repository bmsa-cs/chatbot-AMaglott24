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
  if hru == "Good" or hru =="good":
    print("I'm happy to hear that! I am doing well too.")
  elif hru == "Bad" or hru == "bad":
    print("Oh, I'm sorry. Make sure to always reach out to those around you if you need help!")
  elif hru == "Meh" or hru == "meh":
    print("I can understand that. Sometimes life is just life, nothing particularly\ngood or bad about it.")
  else:
    print("I don't understand that emotion, but hopefully it is good!")
  shows=input("Have you been enjoying any good shows lately? If so, what show? ")
  print("")
  if shows == "The Mandalorian" or shows == "The Office" or shows == "Wanda Vision":
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
  favchar = input("What is your favorite character from the show?: ")
  if favchar == "The Mandalorian":
    print("That is my favorite character too!")
  else:
    print("Nice!")
  print("")
  why = input("Is there any particular reason that you liked this show? ")

  why = random.randint(1,3)
  if why == 1:
    print("Those are some good reasons, maybe I will go and watch it!")
    print("\nWell, it was nice talking, "+str(name)+"! I'm going to go watch that show!")
  elif why == 2:
    print("I probably won't watch that, it doesn't seem like my kind of show.\nSounds fun though!")
    print("\nIt was nice talking, "+str(name)+"! I have to go now though. Have a nice day!")
  else: 
    print("That sounds like a must see!")
    print("\nWell, it was nice talking, "+str(name)+"! I'm going to go watch that movie!")

if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()
