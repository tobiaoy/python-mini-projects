import random

def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_num:
            print("That's a little too low")
        elif guess > random_num:
            print("That's a little high")
            
    print(f"You got it bud, it WAS {random_num}")
    #return random_num
    
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high) #randint has a thing where the high and low values can't be right next to each other, wouldn't really be ints at that point
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
            
    print(f"Computer has guessed your num correctly, it was  {guess}")


computer_guess(500)