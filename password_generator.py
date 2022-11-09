import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*0123456789'

def generate_passwords(num, length):
    pwds = []
    
    for pwd in range(num):
        password = ''
        for ch in range(length):
            password += random.choice(chars)
        pwds.append(password)
        
    return pwds

if __name__ == '__main__':
    print('Password Generator\n')
    
    num = input('How many passwords do you need?\n')
    num = int(num)
    length = input('How long do they need to be?\n')
    length = int(length)
    
    passwords = generate_passwords(num, length)
    print('\nYour passwords: \n')
    for p in range(len(passwords)): 
        print(f'{passwords[p]}\n')
