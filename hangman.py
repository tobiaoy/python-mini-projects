import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word

def hangman():
    
    word = get_valid_word(words)
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    
    lives = 6
    
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'You have already used: ', ' '.join(used_letters))
        
        #what the current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
            else:
                lives -= 1 # takes away a life if wrong
                print('Letter is not in word.')
        
        elif user_letter in used_letters:
            print("You've already guessed that character. Please try again.")
            
        else:
            print('Invalid character. Please try again')
            
            
    if lives == 0:
        print('You died LOL')
    else:
        print('Congrats, you figured out the word. It was', word)