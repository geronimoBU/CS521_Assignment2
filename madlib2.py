'''
Mad Libs v2
Created by: Alex Geronimo
Last Modified: 6/20/17

Items needed: 
1) Folder labeled as 'resources' inside of the current working directory.
2) Four .csv files named 'nouns.csv' 'verbs.csv' 'adjectives.csv' 'sentences.csv' inside of 'resources' folder. 
   Each .csv file contains list of string items. 

Program info: 
Upon execution, the program will ask for a user name. If the user name is new (.csv file in 'references') a new one will be created.
User will then be asked to enter a number. That number will be used to select a noun, verb, and adjective and put it into a sentence. 
Input y to continue or n to exit. 
Upon exit, the new madlib sentences will be appended to the previously saved madlib game. Unless a new user was createt, it will add 
the new madlib sentences to the new user .csv file.
'''

import os
import random
import csv

def load_csv_to_list(path_to_file):
  #Validate Path to file exists
    if os.path.exists(path_to_file) == True:
        path = path_to_file
    else:
        return "Error: Path to file does not exist"

  #Validate file exists
    if os.path.isfile(path_to_file) == True:
        path = path_to_file
    else:
        return "Error: File inside path does not exist."

  #Return a list of items from file
    lst = []
    file = open(path, newline= '')
    reader = csv.reader(file)
    for row in reader:
        lst.append(row[0])

    return lst # Works

def shuffle(sequence):
    'Returns a shuffled list'

   #Write the code that will take a list and shuffle it randomly
    shuf_list = random.sample(sequence, len(sequence))
    return shuf_list  # Works

def load_mad_lib_resource(path_to_resource):
  #Call load_csv_to_list
    lst = load_csv_to_list(path_to_resource)

  #Verify the file exists
    if isinstance(lst, list):
        valid_lst = lst
    else:
        return "Error: Please load an object of type list"

  #Return a tuple of the shuffled list
    shuf_lst = shuffle(valid_lst)
    final_lst = []
    for item in shuf_lst:
        tup = tuple(item.split(","))
        final_lst.append(tup[0])

    return final_lst # Works

def play_game(lower_bound, upper_bound):

    game = True
    while game == True: # Game Loop
        print("")
        print("Game loading..."'\n')
        print("Welcome to Mad Libs"'\n')

        madlib_final = []
        userinput = []

    # Function for User Input & Validation - input arg = prompt text to user. body = check if positive, integer, and index bounds. return = userinput
        def inputNumber_Val(num_prompt):
            while True:
                try:
                    userinput = int(input(num_prompt)) # User input from function argument prompt

                    # Check if integer is positive or zero
                    if userinput >= 0:
                        userinput = userinput
                    else:
                        num_prompt = ("Error: Please enter a positive number: "'\n')
                        continue

                    # Check that the user input does not exceed index bounds in either sentences, nouns, verbs or adjs
                    if userinput <= upper_bound:
                        userinput = userinput
                    else:
                        num_prompt = ("Error: Please enter a number less than " + str(upper_bound) + ": "'\n')
                        continue

                except ValueError:
                    num_prompt = ("Not an integer! Try again: "'\n')
                    continue

                else:
                    return int(userinput)

    # Inner game loop - as long as user input DOES NOT EQUAL "n" continue writing to madlib final list
        while userinput != "n":
            userinput = inputNumber_Val("Please provide a number between {} and {}".format(lower_bound, upper_bound) + ": "'\n')

            def madlib_index(list): # If user input exceeds index dimensions of list, use remainder as index number
                if userinput < (len(list)):
                    ind_var = userinput
                    return ind_var
                else:
                    ind_var = userinput % len(list)
                    return ind_var

            # Index for each list
            sent_ind = madlib_index(SENTENCES)
            noun_ind = madlib_index(NOUNS)
            verb_ind = madlib_index(VERBS)
            adj_ind = madlib_index(ADJECTIVES)

        # Insert selected noun, verb, and adj into sentence
            madlib = (SENTENCES[int(sent_ind)].format(ADJECTIVES[int(adj_ind)],NOUNS[int(noun_ind)],VERBS[int(verb_ind)]))

        # Check if anything inside of final list and check if the resulting sentence is unique to .append list (final)
            if not madlib_final:
                madlib_final = [madlib]
            elif madlib in madlib_final:
                if len(madlib_final) == upper_bound:
                    print("All possible sentences created"'\n')
                    break
                else:
                    print("This sentence has been used already, enter another number: ")

                    continue
            else:
                madlib_final.append(madlib)  # Add current madlib to madlib_final list

        # Print current mad lib to user: elem on separate lines
            print("Current MadLib: "'\n')
            for elem in madlib_final:
                print(elem)

        # Ask user if they would like to continue playing & validate input
            print("")
            next = input("Would you like to keep playing? (enter 'y' or 'n'): "'\n')
            if len(madlib_final) == upper_bound:
                    print("All possible sentences created"'\n')
                    break
            while next != "n" and next != "y":
                next = input("Please enter either 'y' to continue playing or 'n' to exit: "'\n')
            if next == "n":
                userinput = "n"
            else:
                continue
        print("")
        print("Thanks for playing")

        madlib_final_tup = []
        for items in madlib_final:
            items = tuple(items.split(':'))
            madlib_final_tup.append(items)

        return madlib_final_tup


    game = False
    return madlib_final_tup


# GET THE LISTS FROM THE FILES
cwd = os.getcwd()
filepath = os.path.join(cwd,"resources")

SENTENCES = load_mad_lib_resource(os.path.join(filepath, 'sentences.csv'))
NOUNS = load_mad_lib_resource(os.path.join(filepath, 'nouns.csv'))
VERBS = load_mad_lib_resource(os.path.join(filepath, 'verbs.csv'))
ADJECTIVES = load_mad_lib_resource(os.path.join(filepath, 'adjectives.csv'))

#VERIFY THE LISTS EXIST
if not SENTENCES:
    print("Error: Sentences file not found")
    sys.exit()

if not NOUNS:
    print("Error: Nouns file not found")
    sys.exit()

if not VERBS:
    print("Error: Verbs file not found")
    sys.exit()

if not ADJECTIVES:
    print("Error: Adjectives file not found")
    sys.exit()

# Boundaries
MIN_VALUE = 0
MAX_VALUE = max(len(SENTENCES),len(NOUNS),len(VERBS),len(ADJECTIVES),)-1

#PROMPT FOR USERNAME

username = input("Please enter a username: \n")

#VERIFY THE A USER NAME WAS ENTERED ELSE EXIT THE PROGRAM
if not username:
    print("Please enter a username: \n")
    sys.exit()

'''
1) FIND OUT IF THERE IS AN EXISTING USER SAVED GAMES
2) GET THE USER'S SAVED GAMES IF IT EXISTS
3) SORT THE USER SENTENCES
'''

user_filepath = os.path.join(cwd, "resources",username + ".csv")

if os.path.exists(user_filepath) == True:  # Reads previous user mad lib
    with open (user_filepath, 'r') as fh:
        reader = csv.reader(fh)
        user_sentences = []
        for row in reader:
            user_sentences.append(tuple(row))
        '''
        What the next line does is take the unsorted user sentences and
        sorts all of the sentences based on the integer values from
        the 2nd item in the tuple, or index[1]
        '''
        user_sentences = sorted(user_sentences, key=lambda x: int(x[1]))

        print("User: '{0}' now loaded".format(username))

else: # Creates new user mad lib .csv file
    with open (user_filepath, 'x') as fh:
        reader = csv.reader(fh)
        user_sentences = []
        print("New user: '{0}' has been created".format(username))


if user_sentences != []: # New users will skip this. Past users will return madlib items from csv
    print("")
    print("Loaded madlib from file: "'\n')
    for items in user_sentences:
        print(items[0])

#CALL PLAY GAME FUNCTION!

new_madlib = play_game(MIN_VALUE,MAX_VALUE)

'''
Check if new madlib sentences are in previous games:
If a sentence is the same, it will remove it from the
new madlib list and it will not get written to the csv
'''
for sent in new_madlib:
    for user_sent in user_sentences:
        if sent[0] in user_sent:
            new_madlib.remove(sent)

# Prints the new items being added to the user madlib file
print("")
print("New items added: \n")
for items in new_madlib:
    print(items[0])
print("")
# Add new madlib sentences to previously saved csv data
for item in new_madlib:
    user_sentences.append(item)

# Create final madlib var
final_madlib = user_sentences


def write_csvFile (path, list):
    file = open (path, "w")
    length = len (list)

    for idx in range (length):
        line = list [idx]
        if "[" in line:
            line = line [1:-1]

        file.write ("{},{}\n".format (line[0], idx + 1))

    file.close ()

'''
Write final madlib list to user csv file
Format: 1st Col - sentences , 2nd Col - row number (idx + 1)
'''
write_csvFile(user_filepath, final_madlib)

print("Good Bye")

