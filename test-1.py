import  pyfiglet
import random
import numpy



#---------------------------------------------------------------------------------------------------------------------------------
# function -1  creat a big ASCII code for heading

def ascii_code(x):
    print("-"*69)
    code = pyfiglet.figlet_format(x, font='standard')
    print(code)
    print("-"*69)

#---------------------------------------------------------------------------------------------------------------------------------
# function -2 number guessing function

def guess(y,z):
    number = random.randint(y,z)
    return number


#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# function 3 ask for level HARD or EASY

def game_level():
    while True:
        level = input("⚫ CHOOSE YOUR LEVEL [HARD/EASY] = ").lower()
        print("-"*69)
        if level not in ['easy','hard']:
            print("⚫ ENTER A VALID INPUT !")
            print("-"*69)
        else:
            break

    return level

#---------------------------------------------------------------------------------------------------------------------------------
# function - 4  giving the number of life on the basis of level choose









#-----------------------------------------------------------------------------------------------------------------
# calling functions -1

ascii_code("GUESS THE NUMBER")

number = guess(10, 100)
level = game_level()


#---------------------------------------------------------------------------------------------------------------------

# function -5 giving number of life on the basis of level user choose eg- HARD = 5 life  , EASY = 10 life


def number_of_life(level):
    #print("-"*69)
    if level == "easy":
        print("-"*50 + "❤   "*9 +"❤"+ "-"*50)
        print("-"*50 +"-"* 14 + "YOU HAVE 10 LIFE" + "-"*14 + "-"*50)
    elif level == "hard":
        print("-"*50 + "❤   "*4+"❤" + "-"*50)
        print("-"*49 + "⚫ YOU HAVE 5 LIFE" + "-"*50)
    else:
        print("YOU HAVE ENTER SOME WRONG LEVEL ! [PLEASE ENTER ONLY EASY/HARD]")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Function -5 taking input of guessed number
def user_guess():
    while True:
        try:
            guess_the_number = int(input('⚫ GUESS THE NUMBER [1,100] = '))
            print("-"*69)
            if guess_the_number not in range(101):
                print("INVALID GUESS PLEASE GUESS A VALID NUMBER BETWEEN [1,100]!")
                print("-"*69)
            else:
                break

        except:
            print("-"*69)
            print("ENTER A VALID GUESS ! ")
            print("-"*69)




    #return guess_the_number


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# function - 6


#---------------------------------------------------------------------------------------------------------------------------------------------------------------

number_of_life(level)
user_guess()