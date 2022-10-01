import random

top_range = input("enter a number: ")

if top_range.isdigit():
    top_range = int(top_range)
    
    if(top_range <= 0):
        print("please enter positive number next time")
        quit()
else:
    print("please enter a number next time")
    quit()

r_num=random.randint(0,top_range)    #randint will include 11 also and randrange will not
count=0
while(True):
    user_guess = input("make a guess :")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please enter a number next time")
        continue
    
    if user_guess == r_num:
        count+=1
        print("you got it right!!")
        break
    else:
        if(user_guess > r_num):
            print("the number is smaller")
        else:
            print("the number is bigger")
        count+=1
        print("you got it wrong!!")
    
print("you got it right in " +str(count)+ " guesses")
    