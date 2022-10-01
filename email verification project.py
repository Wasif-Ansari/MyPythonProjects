
email = input(" Enter your Email : ") #g@a.in
k,j,d=0,0,0
if(len(email)>=6): #length error
    if(email[0].isalpha()): #first is char
        if ("@" in email) and (email.count("@")==1): #@ and its count
            if (email[-4]==".") ^ (email[-3]=="."): #XOR for .
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha() and i==i.upper():
                        j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d==1
                if(k==1 or j==1 or d==1):
                    print(" wrong Email 5")
            else:
                print(" wrong Email 4")
        else:
            print(" wrong Email 3")
    else:
        print(" wrong Email 2 ")
else:
    print(" wrong Email 1 ")



