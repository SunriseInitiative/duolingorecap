import resources
import sys
import os
import time
import random

def choiceInput(prompt, choices):
    while True:
        print(f"Choices: {', '.join(choices)}")
        choice = input(prompt)
        if choice in choices:
            return choice

print(f"Language = {resources.language}")
print(f"Version = {resources.version}")
debugMode = True
print("Program starting...")
time.sleep(1)

if debugMode:
    print("Debug mode enabled")

practiceMode = choiceInput("Do you want to practice: ", ["Characters", "Words"])

if practiceMode == "Characters":
    while True:
        if (random.randint(0, 1) == 0):
            char = random.randint(0, len(resources.characters) - 1)
            print(resources.characters[char])
            time.sleep(1)
            if debugMode:
                print(f"Character = {resources.characters[char]}")
                print(f"Character number = {char}")

            charIn = input("English character: ")

            if debugMode:
                print(f"Character input = {charIn}")
            
            if charIn == resources.enChar[char]:
                print("Correct!")
            else:
                print(f"Wrong! The correct answer was {resources.enChar[char]}")
            time.sleep(0.1)
            
        else:
            char = random.randint(0, len(resources.enChar) - 1)
            print(resources.enChar[char])
            time.sleep(1)
            if debugMode:
                print(f"Character = {resources.enChar[char]}")
                print(f"Character number = {char}")

            charIn = input("Japanese character: ")

            if debugMode:
                print(f"Character input = {charIn}")
            
            if charIn == resources.characters[char]:
                print("Correct!")
            else:
                print(f"Wrong! The correct answer was {resources.characters[char]}")
            time.sleep(0.1)
