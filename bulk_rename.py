# will go into a directory and rename all the files in it
import os

def rename(path, name, ext):
    i = 0
    
    for file in os.listdir(path):
        dest = f'{name}{i}.{ext}'
        source = path + file
        dest = path + dest
        os.rename(source, dest)
        i += 1
        
        
if __name__ == '__main__':
    path = input('Please enter your exact file path\n') # we can validate this later
    name = input('What do you want to name the files in this folder? ')
    ext = input('What extension do you want them to have? ')
    
    rename(path, name, ext)
    print('The rename was a success!')
    
    