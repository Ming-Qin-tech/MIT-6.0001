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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    flag = True
    for x in secret_word:
        if x not in letters_guessed:
            flag = False
            return flag
    return flag
    


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    c = ''
    for x in secret_word:
        # print(x)
        
        if x in letters_guessed:
            c = c+x
        else:
            c = c + '_ '
    return c


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    c = ''
    for x in string.ascii_lowercase:
        if x not in letters_guessed:
            c = c + x
    return c
    
    

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # wordlist = load_words()
    # secret_word = choose_word(wordlist)
    print("Welcome to the game Hangman!")
    length = len(secret_word)
    guesses_remaining = 6
    warnings_remaining = 3
    print("I am thinking of a word that is ", length, " letters long.")
    print("You have ", warnings_remaining, " warnings left.")
    print("-------------")
    
    letters_guessed = ''
    # hide_word = get_guessed_word(secret_word, letters_guessed)
    won_flag = False
    while guesses_remaining > 0:
        print("You have ", guesses_remaining, " guesses left.")
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: ", available_letters)
        input_letter = input("Please guess a letter: ")
        input_letter = input_letter.lower()
        once_again = False
        if input_letter in letters_guessed:
            once_again = True
        letters_guessed = letters_guessed + input_letter
        if input_letter in secret_word and once_again == False:
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            if '_' not in get_guessed_word(secret_word, letters_guessed):
                won_flag = True
                break
        elif input_letter.isalpha() == False:
            
            print("Oops! That is not a valid letter.", end=(""))
            if warnings_remaining > 0:
                warnings_remaining = warnings_remaining - 1
                print(" You have ", warnings_remaining, " warnings left: ", get_guessed_word(secret_word, letters_guessed))
            else:
                print(" You have no warnings left so you lose one guess: ", get_guessed_word(secret_word, letters_guessed))
                guesses_remaining = guesses_remaining - 1
        elif once_again == True:
            warnings_remaining = warnings_remaining - 1
            print("Oops! You've already  guessed that letter. You now have ", warnings_remaining, " warnings: ", get_guessed_word(secret_word, letters_guessed))
            once_again = False
        else:
            if input_letter in 'aeiou':
                guesses_remaining = guesses_remaining - 2
            else:
                guesses_remaining = guesses_remaining - 1
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
        
        print("------------")
    if won_flag == True:
        print("Congratulations, you won!")
        temp = set(secret_word)
        temp_len = len(temp)
        score = temp_len * guesses_remaining
        print("You total score for this game is: ", score)
    else:
        print("Sorry, you ran out of guesses. The word was ", secret_word)
            
    



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
    my_word = my_word.replace(" ","")
    flag = True
    if len(my_word) != len(other_word):
        flag = False
        return flag
    for index in range(len(my_word)):
        if my_word[index] == '_':
            continue
        else:
            if my_word[index] != other_word[index]:
                flag = False
    return flag



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    flag = True
    for word in wordlist:
        if match_with_gaps(my_word, word):
            flag = False
            print(word, end=" ")
    if flag:
        print("No matches found")
    print("")
            



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
    print("Welcome to the game Hangman!")
    length = len(secret_word)
    guesses_remaining = 6
    warnings_remaining = 3
    print("I am thinking of a word that is ", length, " letters long.")
    print("You have ", warnings_remaining, " warnings left.")
    print("-------------")
    
    letters_guessed = ''
    # hide_word = get_guessed_word(secret_word, letters_guessed)
    won_flag = False
    while guesses_remaining > 0:
        print("You have ", guesses_remaining, " guesses left.")
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: ", available_letters)
        input_letter = input("Please guess a letter: ")
        input_letter = input_letter.lower()
        once_again = False
        if input_letter == '*':
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
        if input_letter in letters_guessed:
            once_again = True
        letters_guessed = letters_guessed + input_letter
        if input_letter in secret_word and once_again == False:
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            if '_' not in get_guessed_word(secret_word, letters_guessed):
                won_flag = True
                break
        elif input_letter.isalpha() == False:
            
            print("Oops! That is not a valid letter.", end=(""))
            if warnings_remaining > 0:
                warnings_remaining = warnings_remaining - 1
                print(" You have ", warnings_remaining, " warnings left: ", get_guessed_word(secret_word, letters_guessed))
            else:
                print(" You have no warnings left so you lose one guess: ", get_guessed_word(secret_word, letters_guessed))
                guesses_remaining = guesses_remaining - 1
        elif once_again == True:
            warnings_remaining = warnings_remaining - 1
            print("Oops! You've already  guessed that letter. You now have ", warnings_remaining, " warnings: ", get_guessed_word(secret_word, letters_guessed))
            once_again = False
        else:
            if input_letter in 'aeiou':
                guesses_remaining = guesses_remaining - 2
            else:
                guesses_remaining = guesses_remaining - 1
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
        
        print("------------")
    if won_flag == True:
        print("Congratulations, you won!")
        temp = set(secret_word)
        temp_len = len(temp)
        score = temp_len * guesses_remaining
        print("You total score for this game is: ", score)
    else:
        print("Sorry, you ran out of guesses. The word was ", secret_word)
            



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
