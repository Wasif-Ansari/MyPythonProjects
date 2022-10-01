from time import * #due to star no need to use alias (as)
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error+=1
        except:
            error+=1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)
while True:
    check = input("READY FOR THE TEST: yes / no : ")
    if(check.lower() == "yes"):
        test = ["A paragraph is a self contained unit of discourse in writing dealing with a particular point or idea.",
        "my name is wasif ansari","this is my project of speed calculator"]

        test1 = r.choice(test) #choosing one randomly from a list

        print("     ****** typing speed ******")
        print(test1)
        print()
        print()
        time_1 = time()
        testinput = input(" Enter the string : ")
        time_2 = time()

        print("Speed : ",speed_time(time_1,time_2,testinput),"letters/sec")
        print("Error : " , mistake(test1,testinput))
    elif(check.lower() == "no"):
        print(" Thank you!")
        break
    else:
        print(" wrong input! ")