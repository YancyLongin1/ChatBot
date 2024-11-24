#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 13:00:32 2023

@author: yancylongin
"""
#  This is a simple Eliza-like chatbot in Python 3.x.
# The chatbot can recognize and respond to user's feelings, certain general states,
# and verbs ending in 'ed'. It also recognizes relationship labels like "mother", "father", etc.

import re
import random

def main():
    """Main function that handles the dialogue flow."""
    greet_user()

    while True:
        user_input = input("> ")  # User's input as a string

        if user_input.lower() == 'bye':
            print("Goodbye!")
            break

        process_input(user_input)

def greet_user():
    """Greet the user and ask for their name."""
    print("Hello! What is your name?")
    
    while True:
        user_input = input("> ")  # User's input as a string
        name_search = re.search(r'\b(I am|my name is)\s*(\w+)', user_input, re.IGNORECASE)
        
        if name_search:
            name = name_search.group(2)  # Extracted name
            print(f"Hello {name}. How are you feeling today?")
            break

def process_input(user_input):
    """Process user input and respond appropriately."""
    # Search for specified feelings like sad, happy, etc.
    feeling_search = re.search(r'\b(sad|happy|joy|joyful|joyfulness|saddened)\b', user_input, re.IGNORECASE)
    
    # Search for general feelings like ok, good, bad
    general_feeling_search = re.search(r'\b(ok|good|bad)\b', user_input, re.IGNORECASE)
    
    # Search for verbs ending in 'ed'
    verb_ending_with_ed = re.search(r'\b(\w+ed)\b', user_input, re.IGNORECASE)
    
    # Search for relationship labels like mother, father, etc.
    relationship_search = re.search(r'\b(mother|mom|father|dad|brother|sister|friend)\b', user_input, re.IGNORECASE)

    if feeling_search:
        feeling = feeling_search.group(1).lower()  # Extracted feeling
        respond_to_feelings(feeling)
        
    elif general_feeling_search:
        general_feeling = general_feeling_search.group(1).lower()  # Extracted general feeling
        respond_to_general_feelings(general_feeling)
        
    elif verb_ending_with_ed:
        verb_ed = verb_ending_with_ed.group(1)  # Extracted verb ending with 'ed'
        infinitive_verb = verb_ed[:-1]  # Infinitive form of the verb
        print(f"Why did it {infinitive_verb} you?")
        
    elif relationship_search:
        relationship = relationship_search.group(1).lower()  # Extracted relationship label
        print(f"How is your {relationship}?")

    else:
        print("I see. Please go on.")

def respond_to_feelings(feeling):
    """Respond based on detected feelings like sad, happy, etc."""
    if 'sad' in feeling:
        print("I'm sorry to hear that you're sad. Would you like to talk about it?")
    elif 'happy' in feeling or 'joy' in feeling:
        print("That's great to hear! What's making you feel this way?")

def respond_to_general_feelings(feeling):
    """Respond based on general feelings like ok, good, bad."""
    if 'ok' in feeling:
        print("Just ok? What's on your mind?")
    elif 'good' in feeling:
        print("That's good to hear! What's making your day good?")
    elif 'bad' in feeling:
        print("I'm sorry to hear that. What happened?")

if __name__ == '__main__':
    main()
