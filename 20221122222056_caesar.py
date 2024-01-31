"""
David Cimpoiasu, 2130140
420-LCU Computer Programming, Section 1
R. Vincent, instructor
Assignment 4
"""
#*** You will add your code to this file. ***

import string

### DO NOT MODIFY THIS FUNCTION ###
def read_word_list(file_name):
    '''
    file_name (str): the name of the file containing the list of words
    to load.
    
    Returns: a set of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    in_file = open(file_name, 'r') # in_file: file
    line = in_file.readline()      # line: str
    word_list = line.split()       # word_list: list of str
    in_file.close()
    return frozenset(word_list)    # creates an immutable set.

N_LETTERS = len(string.ascii_lowercase)
VALID_WORDS = read_word_list('words.txt')

#Test for string by doing a dictionary
a = string.ascii_lowercase + string.ascii_uppercase
MAIN = {}
A = []
for i in range(len(a)):
    A.append(a[i])
z = 0
for i in A:
    MAIN[z]= i
    z += 1

# IMPLEMENT THIS FUNCTION
def create_shift_table(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        
        
    shift (int): the amount by which to shift every letter of the 
    alphabet, 0 <= shift < N_LETTERS. If shift is less than zero or
    greater than or equal to N_LETTERS, this function should return
    None.

    Returns: a dictionary mapping a letter (str) to another
             letter (str), for all lower and upper case letters.
    '''
    # YOUR CODE HERE
    PA = A.copy() #Copy the text
    
    if type(shift) != int:
        return 'INVALID' #Make sure its a int
    
    if not 0<= shift < N_LETTERS: # Make sure the shift is valid
        return None
    GA = []
    G = []
    for i in range(shift, 26):
        G.append(i) # Makes a list in order of the shift
    for i in range(shift):
        G.append(i)
    for i in G:
        GA.append(PA[i]) # Appends the lower alphabet using the list we made
    GD = []
    for i in range(26+shift, 52):
        GD.append(i)
    for i in range(26, 26+shift):
        GD.append(i) # makes a second list for the higher alphabet
    for i in GD:
        GA.append(PA[i]) # Appends the higher alphabet to GA
    DIFF = dict(zip(PA, GA)) # Makes the dictionary using zip of alphabet and shifted alphabet
    return DIFF

### IMPLEMENT THIS FUNCTION
def apply_shift(original_text, shift):
    '''
    Applies the Caesar Cipher to original_text with the input shift.
    Creates a new string that is original_text shifted down the
    alphabet by some number of characters determined by the input shift        
    shift (int): the shift with which to encrypt the message.
    0 <= shift < N_LETTERS

    Returns: the message text (str) in which every character is shifted
             down the alphabet by the input shift
    '''
    # YOUR CODE HERE
    LO = create_shift_table(shift) # creats the reference dictionary
    L = list(original_text) # makes a list of the text cuz its mutable
    for i in range(len(L)):
        ui = L[i] # finds the letter
        if ui == ' ': # no need but just to make sure
            continue
        elif ui.isalpha(): # changes only alphabet
            L[i] = LO[ui] # changes the list using the dictionary
    XX = ''.join(L) # joins the dictionary into a str
    return XX
    

### IMPLEMENT THIS FUNCTION
def encrypt_message(original_text, shift):
    '''
    Used to encrypt the message using the given shift value.
        
    Returns: The encrypted string.
    '''
    # YOUR CODE HERE
    X = apply_shift(original_text, shift) # uses the internal def to respond to this def
    return X

### IMPLEMENT THIS FUNCTION
def is_word(word):
    '''
    Determines if word is a valid word, ignoring
    capitalization, punctuation, and possible spaces.
        
    word (str): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word('Bat')
    True
    >>> is_word('asdf')
    False
    '''
    # YOUR CODE HERE
    f5 = string.punctuation # assing the punctuation
    f6 = string.whitespace # assing the whitespace
    X = word.strip(f5) # strip the punctuation
    D = X.strip(f6) # strip the whitespace
    FFG = D.lower()# lowers the word
    if FFG in VALID_WORDS: #checks if in valid_words 
        return True
    else:
        return False # if not in Valid word, returns false

### IMPLEMENT THIS FUNCTION ###
def decrypt_message(cipher_text):
    '''
    Decrypt cipher_text by trying every possible shift value
    and find the "best" one. We will define "best" as the shift that
    creates the maximum number of real words when we use apply_shift(shift)
    on the text. If s is the original shift value used to encrypt
    the message, then we would expect N_LETTERS - s to be the best shift value 
    for decrypting it.

    Note: if multiple shifts are equally good such that they all create 
    the maximum number of words, you may choose any of those shifts (and 
    their corresponding decrypted messages) to return

    Returns: a tuple of the best shift value used to decrypt the message
    and the decrypted message text using that shift value.
    '''
    # YOUR CODE HERE
    HH = [] # empty list for comparison for each tries 
    for i in range(N_LETTERS): # applying each tries
        H = 0 # setting base value
        x = apply_shift(cipher_text, i) # trying the the shift
        s = x.split()
        for I in s:
            if is_word(I): # Testing the word, if valid word, add 1 to base value
                H += 1
        HH.append(H) # append the final base value to a list
    HHH = max(HH) # finding the best value
    GGG = HH.index(HHH) # finding what the shift was for the best value
    LKL = apply_shift(cipher_text, GGG) # applying the final shift
    TTT = [GGG, LKL] # making the tuple
    YYY = tuple(TTT)
    return YYY # returning the tuple
            

