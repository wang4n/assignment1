# -*- coding: utf-8 -*-

# Description:
#
# This is the final version guess number game demo program
# The entry point of program starts with main() and being verified
# by __name__.
# The computer generated number is from 1 to x where x is passed
# from guess(x) and x is set to 10 in this listing.
#
# Author: John Nichpornkul
# Date: 18 Oct. 2021

import random   # import the random number package

def main():
    guess(10)
    
    
    
    
def guess(x):
    random_number = random.randint(1, x)
    arr = [random_number]
    guess = 0   
    while guess != random_number:
        guess = int(input("Enter your guess number, please: "))
        arr.append(guess)
        while arr[0] - arr[1] > 0:
            print('too small')
            break
        while arr[0] - arr[1] < 0:
            print('too high')
            break;
        arr.pop()

        
        
      
            
    print("You have guessed the number", random_number, "correctly!!")
    
if __name__ == '__main__':
    main()