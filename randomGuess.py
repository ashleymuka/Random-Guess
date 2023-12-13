'''
Author: Ashley Muka
Assignment Title: Random Guess
Assignment Description:implemet the number_guess() function to output
if the number guessed is too low, too high, or correct
Due Date:09/18/2023
Date Created:09/18/2023
Date Last Modified:09/18/2023

'''

import random

#data abstraction
def number_guess(num):
    
    rand_num = random.randint(1, 100)
    
#output
    if num < rand_num:
        print(f'{num} is too low. Random number was {rand_num}.')
    elif num > rand_num:
        print(f'{num} is too high. Random number was {rand_num}.')
    else:
        print(f'{num} is correct!')

if __name__ == "__main__":
#input and process   
    random.seed(900)

    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        num = int(token)
        number_guess(num)
