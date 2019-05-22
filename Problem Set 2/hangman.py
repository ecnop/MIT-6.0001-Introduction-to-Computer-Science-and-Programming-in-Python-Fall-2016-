# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    is_word_guessed = True
    for i in secret_word:
        if i not in letters_guessed:
            is_word_guessed = False
            break
    return is_word_guessed


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ''
    for i in secret_word:
        if i in letters_guessed:
            guessed_word += i
        else:
            guessed_word += '_ '
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    allLower = string.ascii_lowercase
    strAvailable = ""
    for i in allLower:
        if i not in letters_guessed:
            strAvailable += i
            
    return strAvailable

def unique_letters(secret_word):
    list_unique_letters = []
    for i in secret_word:
        if i not in list_unique_letters:
            list_unique_letters.append(i)
    return len(list_unique_letters)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    

    #Useful variables:
    
    guesses_left = 6    #Number of guesses left initializes at 6
    length_word = len(secret_word)  #Number of letters the secret word contains
    letters_guessed = [] #Creating a list of the guessed letters initialized empty
    warnings = 3 #Creates the warning variable and initializes it at 3
    vowels = 'aeiou'
    
    #Output of the game in the beginning of the game
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",length_word,"letters long.")
    print("You have",warnings," warnings left.")
    print("-------------")
    
    #Main loop to get the game going, exits the loop if the player guessed the word or exhausted his guesses
    while (not is_word_guessed(secret_word, letters_guessed) and guesses_left > 0):
        
        #Initial message every turn telling the player how many guesses he has left and what are the available letters to guess
        if guesses_left > 1:
            print("You have",guesses_left,"guesses left.")
        else:
            print("You have",guesses_left,"guess left.")
        print("Available letters:",get_available_letters(letters_guessed))
        
        
        #Get the new guess from the player 
        newGuess = input("Please guess a letter: ")
       
        #branching algorithms to test if the input is valid or has already been guessed and counts warnings in order to give some tolerance for incorrect inputs
        if not str.isalpha(newGuess):
            if warnings > 0:
                warnings -= 1
                print("Oops! That is not a valid letter. You have",warnings,"warnings left:",get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                continue
            else:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                continue
        elif len(newGuess) > 1:
            if warnings > 0:
                warnings -= 1
                print("Oops! That is more than one letter. You have",warnings,"warnings left:",get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                continue                
            else:
                guesses_left -= 1
                print("Oops! That is more than one letter. You have no warnings left so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                continue
        elif newGuess in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print("Oops! You've already guessed that letter. You have",warnings,"warnings left:",get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                continue
            else:
                guesses_left -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                continue
        
        
        #Add the new guess to the list of letters guessed
        newGuess = newGuess.lower()
        letters_guessed.append(newGuess)
        
        #If statement in case the user guessed appropriately or not
        if newGuess in secret_word:
            print("Good guess:",get_guessed_word(secret_word,letters_guessed))
        else:
            #The user loses 2 points if he guessed a vowel wrong and one point if he guessed a consonant wrong
            if newGuess in vowels:
                print("Oops! That letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
                guesses_left -= 2
            else:
                print("Oops! That letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
                guesses_left -= 1
        
        #Separating dashes between turns
        print("-------------")

    #Number of unique letters in the secret word --> to calculate the total score
    
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations! You won!")
        print("Your total score for this game is:",unique_letters(secret_word)*guesses_left)
    else:
        print("Sorry, you ran out of guesses. The word was:",secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    a = ""
    
    #Remove spaces from my_word to be able to compare it with other_word
    for i in my_word:
        if i != " ":
            a += i
        
#    print(a)
    
    #Compare the lengths of the words and return false if they have different lengths
    if len(a) != len(other_word):
#        print("Words have different lengths.")
        return False
    
    #Create a variable that is initialized at True and change to False when
    #there is a disparity between the actual letters of the word being guessed
    #and the other word
    all_match = True
    
    for i in range(len(a)):
        if a[i] in string.ascii_lowercase and a[i] != other_word[i]:
            all_match = False
    
    return all_match
                

#w1 = 'b_ _ _ _ l_ '
#w2 = 'baggage'
#x = match_with_gaps(w1,w2)
#print(x)



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matching_words = ""
    
    for i in wordlist:
        if match_with_gaps(my_word,i):
            matching_words += i + " "
        
    print(matching_words)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    #Useful variables:
    
    guesses_left = 6    #Number of guesses left initializes at 6
    length_word = len(secret_word)  #Number of letters the secret word contains
    letters_guessed = [] #Creating a list of the guessed letters initialized empty
    warnings = 3 #Creates the warning variable and initializes it at 3
    vowels = 'aeiou'
    
    #Output of the game in the beginning of the game
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",length_word,"letters long.")
    print("You have",warnings," warnings left.")
    print("-------------")
    
    #Main loop to get the game going, exits the loop if the player guessed the word or exhausted his guesses
    while (not is_word_guessed(secret_word, letters_guessed) and guesses_left > 0):
        
        #Initial message every turn telling the player how many guesses he has left and what are the available letters to guess
        if guesses_left > 1:
            print("You have",guesses_left,"guesses left.")
        else:
            print("You have",guesses_left,"guess left.")
        print("Available letters:",get_available_letters(letters_guessed))
        
        
        #Get the new guess from the player 
        newGuess = input("Please guess a letter: ")
       
        #branching algorithms to test if the input is valid or has already been guessed and counts warnings in order to give some tolerance for incorrect inputs
        if not str.isalpha(newGuess):
            if newGuess == "*":
                print("Possible word matches are:")
                show_possible_matches(get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                continue
            elif warnings > 0:
                warnings -= 1
                print("Oops! That is not a valid letter. You have",warnings,"warnings left:",get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                continue
            else:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                continue
        elif len(newGuess) > 1:
            if warnings > 0:
                warnings -= 1
                print("Oops! That is more than one letter. You have",warnings,"warnings left:",get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                continue                
            else:
                guesses_left -= 1
                print("Oops! That is more than one letter. You have no warnings left so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                continue
        elif newGuess in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print("Oops! You've already guessed that letter. You have",warnings,"warnings left:",get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                continue
            else:
                guesses_left -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:",get_guessed_word(secret_word,letters_guessed))
                print("-------------")
                continue
        
        
        #Add the new guess to the list of letters guessed
        newGuess = newGuess.lower()
        letters_guessed.append(newGuess)
        
        #If statement in case the user guessed appropriately or not
        if newGuess in secret_word:
            print("Good guess:",get_guessed_word(secret_word,letters_guessed))
        else:
            #The user loses 2 points if he guessed a vowel wrong and one point if he guessed a consonant wrong
            if newGuess in vowels:
                print("Oops! That letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
                guesses_left -= 2
            else:
                print("Oops! That letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
                guesses_left -= 1
        
        #Separating dashes between turns
        print("-------------")

    #Number of unique letters in the secret word --> to calculate the total score
    
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations! You won!")
        print("Your total score for this game is:",unique_letters(secret_word)*guesses_left)
    else:
        print("Sorry, you ran out of guesses. The word was:",secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
