import random # this func. picks the random values to avoid cheating

def gameWin (comp, you):
    if comp == you:
        return None
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
        
print("Comp Turn : Snake(s) Water(w) or Gun(g)?") # 1
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your turn : Snake(s) Water(w) or Gun(g)?") # 2
a = gameWin(comp,you)

print(f"Computer chose {comp}") # 3
print(f"You chose {you}") # 4 

if a == None:
    print("The game is a tie!")
elif a == True:
    print("You Win!")
else:
    print("You Lose!")
