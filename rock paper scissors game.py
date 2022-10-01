import random

user_wins = 0
cpu_wins = 0


options = ["rock" , "paper" , "scissors"]

while True:
    user_input = input("enter rock/paper/scissors or q to quit: ").lower()
    
    if(user_input == "q"):
        break
    
    if user_input not in options:
        continue
    
    r_number = random.randint(0,2)
    
    cpu_input = options[r_number]
    print("computer picked", cpu_input +".")
    
    if user_input == "rock" and cpu_input == "scissors":
        print("you won")
        user_wins+=1
    elif user_input == "paper" and cpu_input == "rock":
        print("you won")
        user_wins+=1
    elif user_input == "scissors" and cpu_input == "paper":
        print("you won")
        user_wins+=1
    elif user_input == cpu_input:
        print("its a draw")
    else:
        print("you lost")
        cpu_wins+=1
        
print("you won " , user_wins, "times")
print("computer won", cpu_wins, "times")
print("good bye!!")
