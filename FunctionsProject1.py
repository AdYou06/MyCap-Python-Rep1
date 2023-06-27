'''
task: Write a code to create a function called most_frequent
that takes a string and prints the letters in decreasing order of frequency 
using dictionaries
'''

def most_frequent(string):
    letter_frequency = {}
    
    # Count the frequency of each letter using a dictionary
    for letter in string:
        letter_frequency[letter]= letter_frequency.get(letter, 0) + 1
    
    #sort the letters in decreasing order of frequency    
    sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)
   
    #formatting output string using f string
    for char, value in sorted_frequency:
        print(f"{char} = {value:02}")
       
userInput = input("Enter string: ")
most_frequent(userInput)
