a1=int(input())
a2=int(input())
a3=int(input())
a4=int(input())
a5=int(input())
a6=int(input())
a7=int(input())
a8=int(input())
a9=int(input())
def game():
    print("      *       *      ")
    print("      *       *      ")
    print(f"  {a1}   *    {a2}  *   {a3}  ")
    print("* * * * * * * * * * *")
    print("      *       *      ")
    print("      *       *      ")
    print(f" {a4}    * {a5}     *    {a6} ")
    print("* * * * * * * * * * *")
    print("      *       *      ")
    print("      *       *      ")
    print(f"   {a7}  *    {a8}  *    {a9} ")
def update(pos,symbol):
    global a1,a2,a3,a4,a5,a6,a7,a8,a9
    if pos==1:a1=symbol
    if pos==2:a2=symbol
    if pos==3:a3=symbol
    if pos==4:a4=symbol
    if pos==5:a5=symbol
    if pos==6:a6=symbol
    if pos==7:a7=symbol
    if pos==8:a8=symbol
    if pos==9:a9=symbol
def winner(symbol):
    if a1==symbol and a2==symbol and a3==symbol:
        return True
    if a4==symbol and a5==symbol and a6==symbol:
        return True
    if a7==symbol and a8==symbol and a9==symbol:
        return True
    if a1==symbol and a5==symbol and a9==symbol:
        return True
    if a3==symbol and a5==symbol and a7==symbol:
        return True
    if a1==symbol and a4==symbol and a7==symbol:
        return True
    if a2==symbol and a5==symbol and a8==symbol:
        return True
    if a3==symbol and a6==symbol and a9==symbol:
        return True
def Check(pos):
    if pos<1 or pos>9:return False
    if pos==1 and a1!=1:return False
    if pos==2 and a2!=2:return False
    if pos==3 and a3!=3:return False
    if pos==4 and a4!=4:return False
    if pos==5 and a5!=5:return False
    if pos==6 and a6!=6:return False
    if pos==7 and a7!=7:return False
    if pos==8 and a8!=8:return False
    if pos==9 and a9!=9:return False
    return True
turn="X"
moves=0
while True:
    game()
    print("Player",turn,"turn")
    pos=int(input("Enter a position"))
    if Check(pos)== False:
        print("Invalid")
        continue
    update(pos,turn)
    moves==1
    if winner(turn):
        game()
        print("Player",turn,"wins")
        break
    if moves==9:
        game()
        print("Game draw")
        break
    if turn=="X":turn="O"
    else:turn="X"