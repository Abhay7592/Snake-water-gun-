import random

def gamewin(comp,you):
    if comp == you :
        return None
    ## checking all the possibility with respect to computer 
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
        
    elif comp == 'w':
        if you == 's':
            return True 
        elif you == 'g':
            return False 
        
    elif comp == 'g':
         if you == 's':
             return False 
         elif you == 'w':
             return True 
        

print("Computer turn : Snake(s) Water(w) Gun(g):")

randno = random.randint(1,3)

if randno == 1 :
    comp = 's'
    
elif randno == 2 :
    comp = 'w'

elif randno == 3:
    comp = 'g'

you = input("Your turn : Snake(s) Water(w) Gun(g):")

a = gamewin(comp,you)

print(f"Computer choose: {comp}")
print(f"You have choosen: {you}")

if a == None:
    print("The game was tie !!")
elif a == True :
    print("You won the Game")
else:
    print("You Lost")


print("Thank you for playing Our game")          
          
    