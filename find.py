#This script asks for the name of a file the user needs to search.
#Then asks for the name of a new file to put the search results.
#Then asks what to look for.
#Finally it asks if you would like to drill any farther.
import os
#import sys

def search():
    #get input from the user
    file_name = input('Please enter the name of a file you need me to look at: \n')
    document = open(file_name, 'r').read()
    output_file = input('Please enter a name for a new file for the results: \n')
    key_word = input('Pleasse enter the word(s) or number(s) you are looking for: \n')

    #check to see if the search term is present
    if key_word in document:
        n = document.count(key_word)
        print('I found', key_word, n, 'time.\n')
        print('I\'m going to store the results for you in', output_file, '\n')

        #Pull the lines of the file that match
        with open(file_name, 'r') as fp:
            for line in fp:
                if key_word in line:
                    targets = line
                    outf = open(output_file, 'a')
                    outf.write(targets)
    else:
        print("Sorry", key_word, "was not found in this file.\n")

#run loop, controle operation
x = 'y'
while x == 'y':
    search()
    x = input('Would you like to go again?(FYI, I only understand lower case y): \n')
