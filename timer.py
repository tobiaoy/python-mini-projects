import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60) # look up div mod
        timer = f'{mins} : {secs}'
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
        
    print("Your time is up!")
    
if __name__ == '__main__':
    t = input('Enter the amount of time in seconds: ')
    countdown(int(t))