import random
def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='rock':
        if you=="p":
            return True
        elif you=='s':
            return False
    elif comp == 'paper':
        if you== 's':
            return True
        elif you=='r':
            return False
    elif comp==' scissor':
        if you=='r':
            return False

        elif you=='p':
            return True

randno= random.randint(1, 3)
print("computer's turn: rock(1) paper(2) scissor(3)?\n")
if randno==1:
    comp='rock'
elif randno==2:
    comp = 'paper'
elif randno==3:
    comp='scissor'
    
you= input("player's turn: rock(r) paper(p) scissor(s)?")

a = gameWin(comp,you)
print(f"computer chose : {comp}")
print(f"you chose : {you}")
if a==None:
    print( "the game is tie.") 
elif a:
    print("you win")
else:
    print("you loose")