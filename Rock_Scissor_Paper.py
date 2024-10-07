import random

youstr=input("Enter your choice(R/S/P)=")

computer=random.choice([-1, 0, 1])
youDict={"R":-1,"S":0,"P":1}
reverseDict={-1:"Rock",0:"Scissor",1:"Paper"}

you=youDict[youstr]

print(f"You choose: {reverseDict[you]}\nComputer choose: {reverseDict[computer]}")

if(computer==you):
        print("It's a tie")
else:
     if(computer==-1 and you==0):
        print("you loose")
     elif(computer==-1 and you==1):
            print("you won")
     elif(computer==0 and you==-1):
           print("you won")
     elif(computer==0 and you==1):
           print("you loose")
     elif(computer==1 and you==-1):
           print("you loose")
     elif(computer==1 and you==0):
           print("you won")
     else:
           print("something went wrong!")

