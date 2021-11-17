#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 23:02:18 2021

@author: sirajakmal
"""
import csv 
import matplotlib.pyplot as plt

STOPGAP = ["a", "an", "the", "i", "im", "he", "she", "they", 
           "and", "if", "of", "out", "do", "you", "to", "it",
           "is", "was", "in", "we", "that", "my", "your", "be",
           "on", "this", "me", "are", "what", "with", "but", "youre",
           "so", "oh", "for", "like", "him", "have", "not", "one",
           "too", "just", "dont", "well", "yeah", "all", "let", 
           "about", "go", "can", "at", "hes", "thats", "am", "its",
           "as", "were", ""]



def open_file(filename):
    '''
    
    Parameters
    ----------
    filename : csv
        
    takes in a csv file and creates a list of lists with every line

    Returns
    -------
    list of lists with each line.
    '''

    lines = []
    
    with open(filename) as infile:
        
        csv_reader = csv.reader(infile,delimiter=',')
            
        for line in csv_reader:
            
            lines.append(line)
            
        
    return lines


def lower_case(lines): # part 1 of problem 1
    '''
    

    Parameters
    ----------
    lines : list of lists
         makes every value in lowercase and removes stopgap words

    Returns
    -------
    lowered : list of lists
        list of lists in all lowercase and no stop gap words.

    '''
    lowered = []
     
    for line in lines:
        
        cur_line = []
        
        for word in line:
            
            temp = word.lower()
            
            # Makes sure the word being added is not a stopgap
            
            if temp not in STOPGAP:
                
                cur_line.append(temp)
                
        lowered.append(cur_line)
        
    return lowered




def make_dict(character_name, lower): # part 2 of problem 1
    '''
    

    Parameters
    ----------
    character_name : string
        DESCRIPTION.
    lower : list of lists
        
        creates a word count for the given character in the form of a dictionary.
        Checks each line for character name and then either adds words to dictionary 
        or increase
        count. 

    Returns
    -------
    character_words : dictionary
        word count for a specific character.

    '''
    
    
    character_words = {}
    
    
    for line in lower:
        
        if line[0] == character_name:
            
            name = line.pop(0)
            
            for word in line:
                
                #adding each new word to dictionary or adding to existing value
                
                if word in character_words.keys():
                    
                    character_words[word] += 1
                    
                else:
                    
                    character_words[word] = 1
            line.insert(0, name)
            
    return character_words



def top_words(character): # problem 2
    '''
    

    Parameters
    ----------
    character : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    list_of_words = []
    top_word_list = []
    x = 0
    
    # putting the dictionary into a list of lists
    for key in character:
        
        cur_list = [key, character[key]]
        
        list_of_words.append(cur_list)
        
        # initializing intial top 8 words 
        
    while x < 8:
        
        top_word_list.append(list_of_words[x])
        x += 1
    #checking if a word is in the top word list and if it is not
    # comparing it to each word count and replacing if it is greater
    
    for element in list_of_words:
        
        for i in range(len(top_word_list)):
            
            if element not in top_word_list:
            
                if element[1] > top_word_list[i][1]:
                    
                    top_word_list[i] = element
        
    return top_word_list
    



# problem 3
def plot_words(): 
    '''

    prompts user to choose a character and plots their top words
    Returns
    -------
    None.

    '''
    b99 = open_file("b99_lines.csv")
    b99_lower = lower_case(b99)
    character = input("Pick a character: Holt, Gina, or Terry ")
    name = character.lower()
    if name == "holt":
        character = "Holt"
        dictionary = make_dict('holt', b99_lower)
        
    elif name == "gina":
        character = "Gina"
        dictionary = make_dict('gina', b99_lower)
        
    else:
        character = "Terry"
        dictionary = make_dict('terry', b99_lower)
    top_words_character = top_words(dictionary)
    
    for word in top_words_character:
        plt.bar(word[0],word[1])
        
    plt.title("Top Word Count for " + character)
    
    
    
    


       
def main(): 
    
    b99 = open_file("b99_lines.csv")
    b99_lower = lower_case(b99)
    character_list = {}
    character_list['holt'] = make_dict('holt', b99_lower)
    character_list['gina'] = make_dict('gina', b99_lower)
    character_list['rosa'] = make_dict('rosa', b99_lower)
    plot_words()
  
    
main()
