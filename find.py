#This script asks for the name of a file the user needs to search.
#Then asks for the name of a new file to put the search results.
#Then asks what to look for.
#Finally it asks if you would like to drill any farther.
import os
#import sys

def search():
    #get input from the user
    input_file = input('Please enter the name of a file you need me to look at: \n')
    document = open(input_file, 'r').read()
    n = 0
    search_again = 'y'
    while search_again == 'y':
        key_word = input('Pleasse enter the word(s) or number(s) you are looking for: \n')
        output_file = input_file + key_word
        #print(output_file)
        #output_file = input('Please enter a name for a new file for the results: \n')
        #check to see if the search term is present
        if key_word in document:
            n = counter(document, key_word)
            #n = document.count(key_word)
            print('I found', key_word, n, 'time.\n')
            print('I\'m going to store the results for you in', output_file, '\n')

            #Pull the lines of the file that match
            with open(input_file, 'r') as fp:
                for line in fp:
                    if key_word in line:
                        targets = line
                        outf = open(output_file, 'a')
                        outf.write(targets)
            review_file = input('Would you like to review the revised file? ')
            if review_file == 'y':
                reviewer(output_file, key_word, n)

        else:
            print('Sorry', key_word, 'was not found in', input_file, '.\n')

        search_again = input('Would you like to go again with another SEARCH TERM on this file? \n')

def reviewer(x, z, n):
    #x generally going to be output_file
    print_output = open(x).read()
    print(print_output)
    get_count = 'y'
    while get_count == 'y':
        print("Just FYI,", z, "was found", n, "times above.")
        get_count = input('Would you like to get a count on a search term?(y/n) ')
        if get_count =='y':
            new_term = input('What would you like to look for?: ')
            new_value = counter(print_output, new_term)
            print("I found", new_term, new_value, "times.")

def counter(x, y):
    return x.count(y)
run = 'y'
while run == 'y':
    choice = ''
    print("##############################################################################################################")
    print("Search (1): To enter the main program press 1.  The search function will walk through")
    print("whole process which includes looking through a file and selecting items based on your input.\n")
    print("Review and Count Occurances (2): Press 2 if you are just interested simply knowing the number of ")
    print("times something occurs.")
    print("##############################################################################################################")
    choice = input("Welcome to StringSeacher, above is a list of stuff I can do, please make a selection and press enter: ")
    #run loop, controle operation
    #x = 'y'
    if choice == '1':
        print("You have selected Search, please aswer the following questions.\n")
        search()
        x = input('Would you like to go again with a DIFFERENT FILE?(FYI, I only understand lower case y): \n')
        y = input("Would you like to restart the program?: ")
        if y != 'y':
            break
    if choice == '2':
        print("You have selected Count Occurances, please aswer the following questions.\n")
        RaCC = 'y'
        while RaCC == 'y':
            where = input("What file (full path is best) should I go look at?: ")
            check_this = open(where).read()
            print(check_this)
            rerun_file = 'y'
            while rerun_file == 'y':
                new_term = input('What would you like to look for?: ')
                new_value = counter(check_this, new_term)
                print("I found", new_term, new_value, "times.")
                rerun_file = ("want to count something else in this file? ")
                rerun_file = input("Would you like to search this file for another string?: ")
                if rerun_file != 'y':
                    break
            RaCC = input("Would you like to check another file?: ")
            if RaCC != 'y':
                break

        y = input("Would you like to restart the program?: ")
        if y != 'y':
            break
