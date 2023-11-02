# is a reusable block
'''def my_function():
    x=10
    print(x)
my_function()

def my_function():
    x=10
    y=5
    print(x+y)
my_function()'''


#x is  global variable 
'''x=10
def my_function():
    print(x)

my_function()'''

x=10
def modify_global():
    global x
    x=20
    print(x)
modify_global()


# module
import random

def guess_number():
    return random.randint(1,100) #randint is method

target_number = guess_number()
attempts = 0

while True:
    user_guess = int(input("guess the number:"))
    attempts +=1
    
    if user_guess == target_number:
        print("congress! you guessed the number n",attempts,"attempts.")
        break
    elif user_guess<target_number:
        print("try a higher number")
    else:
        print("try a lower number")


































    