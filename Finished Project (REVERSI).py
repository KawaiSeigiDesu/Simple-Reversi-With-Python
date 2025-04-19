import turtle
from copy import deepcopy
import time

# Animation SCREEN
wn = turtle.Screen()
wn.title("REVERSI")
wn.bgcolor("green")
wn.setup(width=650, height=650)
wn.tracer(0)

#  Membentuk banyak shape(garis,kotak,lingkaran,dll)
def borderline(object,x,y,color,p,l,t):
    border = turtle.Turtle()
    border.shape(object)
    border.color(color)
    if(object!='turtle'):border.fillcolor("")
    border.shapesize(p,l,t)
    border.penup()
    border.goto(x,y)

# Menghitung Jumlah Score dan menyimpan nilai tersebut
def totalscore_pin(scoreP1=0, scoreP2=0):
    global run,turnB,list_black,list_white
    for vertical in range(8):
        for horizontal in range(8):
            if(ball_color[vertical][horizontal]=='b'):
                scoreP1+=1
                list_black.append([vertical,horizontal])

            elif(ball_color[vertical][horizontal]=='w'):
                scoreP2+=1
                list_white.append([vertical,horizontal])
    return scoreP1,scoreP2

# Melakukan check 8 arah dimana akan mendapatkan green navigation yang legal
# (selection untuk di click)
def Check_green_navigation(list_output:list, output1:str, output2:str, turn:str):
    global count_illegal
    count_illegal=-1
    list_selection=[]
    hor = [-1,  0, +1, +1, +1, 0, -1 ,-1]
    ver = [+1, +1, +1, 0, -1, -1,-1, 0]

    for i in range(len(list_output)):
        x,y=list_output[i][0],list_output[i][1]
        if(0<=x<=6):
            l1,l2=x,y
            for j in range(x,7+1): # vertical, middle to down
                if(j+1<8):
                    if(ball_color[j][y]=='temp' and ball_color[j+1][y]==turn
                    )or(ball_color[j][y]==ball_color[j+1][y]==turn
                    )or(ball_color[j][y]==turn and ball_color[j+1][y]=='e'
                    )or(ball_color[j][y]==ball_color[j+1][y]=='e'):
                        break
                    if(ball_color[j][y]==output1)and(ball_color[j+1][y]==output2):
                        list_selection.append([j+1,y])
                        count_illegal+=1
                        break
        if(1<=x<=7):
            l1,l2=x,y
            for j in range(x,0,-1): # vertical, middle to up
                if(j-1>-1):
                    if(ball_color[j][y]=='temp' and ball_color[j-1][y]==turn
                    )or(ball_color[j][y]==ball_color[j-1][y]==turn
                    )or(ball_color[j][y]==turn and ball_color[j-1][y]=='e'
                    )or(ball_color[j][y]==ball_color[j-1][y]=='e'):
                        break
                    if(ball_color[j][y]==output1)and(ball_color[j-1][y]==output2):
                        list_selection.append([j-1,y])
                        count_illegal+=1
                        break

        if(0<=y<=6):
            checking=True
            l1,l2=x,y
            for k in range(y,7+1): # horizontal, middle to right
                if(k+1<8):
                    if(ball_color[x][k]=='temp' and ball_color[x][k+1]==turn
                    )or(ball_color[x][k]==ball_color[x][k+1]==turn
                    )or(ball_color[x][k]==turn and ball_color[x][k+1]=='e'
                    )or(ball_color[x][k]==ball_color[x][k+1]=='e'):
                        break
                    if(ball_color[x][k]==output1)and(ball_color[x][k+1]==output2):
                        list_selection.append([x,k+1])
                        count_illegal+=1
                        break
        if(1<=y<=7):
            l1,l2=x,y
            for k in range(y,0,-1): # horizontal, middle to left
                if(k-1>-1):
                    if(ball_color[x][k]=='temp' and ball_color[x][k-1]==turn
                    )or(ball_color[x][k]==ball_color[x][k-1]==turn
                    )or(ball_color[x][k]==turn and ball_color[x][k-1]=='e'
                    )or(ball_color[x][k]==ball_color[x][k-1]=='e'):
                        break
                    if(ball_color[x][k]==output1)and(ball_color[x][k-1]==output2):
                        list_selection.append([x,k-1])
                        count_illegal+=1
                        break

        if(0<=x<=6)and(0<=y<=6):
            l1,l2=x,y
            while(l1!=7 and l2!=7): # middle to downright
                if(ball_color[l1][l2]=='temp' and ball_color[l1+1][l2+1]==turn
                )or(ball_color[l1][l2]==ball_color[l1+1][l2+1]==turn
                )or(ball_color[l1][l2]==turn and ball_color[l1+1][l2+1]=='e'
                )or(ball_color[l1][l2]==ball_color[l1+1][l2+1]=='e'):
                    break
                if(ball_color[l1][l2]==output1)and(ball_color[l1+1][l2+1]==output2):
                    list_selection.append([l1+1,l2+1])
                    count_illegal+=1
                    break
                l1+=1
                l2+=1
        if(1<=x<=7)and(1<=y<=7):
            l1,l2=x,y
            while(l1!=0 and l2!=0): # middle to upleft
                if(ball_color[l1][l2]=='temp' and ball_color[l1-1][l2-1]==turn
                )or(ball_color[l1][l2]==ball_color[l1-1][l2-1]==turn
                )or(ball_color[l1][l2]==turn and ball_color[l1-1][l2-1]=='e'
                )or(ball_color[l1][l2]==ball_color[l1-1][l2-1]=='e'):
                    break
                if(ball_color[l1][l2]==output1)and(ball_color[l1-1][l2-1]==output2):
                    list_selection.append([l1-1,l2-1])
                    count_illegal+=1
                    break
                l1-=1
                l2-=1

        if(0<=x<=6)and(1<=y<=7):
            l1,l2=x,y
            while(l1!=7 and l2!=0): # middle to downleft
                if(ball_color[l1][l2]=='temp' and ball_color[l1+1][l2-1]==turn
                )or(ball_color[l1][l2]==ball_color[l1+1][l2-1]==turn
                )or(ball_color[l1][l2]==turn and ball_color[l1+1][l2-1]=='e'
                )or(ball_color[l1][l2]==ball_color[l1+1][l2-1]=='e'):
                    break
                if(ball_color[l1][l2]==output1)and(ball_color[l1+1][l2-1]==output2):
                    list_selection.append([l1+1,l2-1])
                    count_illegal+=1
                    break
                l1+=1
                l2-=1
        if(1<=x<=7)and(0<=y<=6):
            l1,l2=x,y
            while(l1!=0 and l2!=7): # middle to upright
                if(ball_color[l1][l2]=='temp' and ball_color[l1-1][l2+1]==turn
                )or(ball_color[l1][l2]==ball_color[l1-1][l2+1]==turn
                )or(ball_color[l1][l2]==turn and ball_color[l1-1][l2+1]=='e'
                )or(ball_color[l1][l2]==ball_color[l1-1][l2+1]=='e'):
                    break
                if(ball_color[l1][l2]==output1)and(ball_color[l1-1][l2+1]==output2):
                    list_selection.append([l1-1,l2+1])
                    count_illegal+=1      
                    break
                l1-=1
                l2+=1
    return list_selection

# Melakukan check 8 arah, dari titik yang telah di click
# apakah ada color yang sama di titik arah tersebut
# agar bisa melakukan reverse atau tidak
def get_legal_reverse(list_output:list, output1:str, output2:str, turn:str):
    global count_illegal, ball_color
    count_illegal=-1
    for i in range(len(list_output)):
        x,y=list_output[i][0],list_output[i][1]
        if(0<=x<=6):
            l1,l2=x,y
            for j in range(x,7+1): # vertical, middle to down
                if(j+1<8):
                    if(ball_color[j][y]=='temp' and ball_color[j+1][y]==turn
                    )or(ball_color[j][y]==ball_color[j+1][y]==turn
                    )or(ball_color[j][y]==turn and ball_color[j+1][y]=='e'
                    )or(ball_color[j][y]==ball_color[j+1][y]=='e'):
                        break
                    if(ball_color[j][y]==output1)and(ball_color[j+1][y]==output2):
                        count_illegal+=1
                        Reversing_Process(list_output, 1, x+1,j+1,1, 0,0,0)
                        break
        if(1<=x<=7):
            l1,l2=x,y
            for j in range(x,0,-1): # vertical, middle to up
                if(j-1>-1):
                    if(ball_color[j][y]=='temp' and ball_color[j-1][y]==turn
                    )or(ball_color[j][y]==ball_color[j-1][y]==turn
                    )or(ball_color[j][y]==turn and ball_color[j-1][y]=='e'
                    )or(ball_color[j][y]==ball_color[j-1][y]=='e'):
                        break
                    if(ball_color[j][y]==output1)and(ball_color[j-1][y]==output2):
                        count_illegal+=1
                        Reversing_Process(list_output, 2, x-1,j-1,-1, 0,0,0)
                        break

        if(0<=y<=6):
            l1,l2=x,y
            for k in range(y,7+1): # horizontal, middle to right
                if(k+1<8):
                    if(ball_color[x][k]=='temp' and ball_color[x][k+1]==turn
                    )or(ball_color[x][k]=='temp' and ball_color[x][k+1]==turn
                    )or(ball_color[x][k]==turn and ball_color[x][k+1]=='e'
                    )or(ball_color[x][k]==ball_color[x][k+1]=='e'):
                        break
                    if(ball_color[x][k]==output1)and(ball_color[x][k+1]==output2):
                        count_illegal+=1
                        Reversing_Process(list_output, 3, y+1,k+1,1, 0,0,0)
                        break
        if(1<=y<=7):
            l1,l2=x,y
            for k in range(y,0,-1): # horizontal, middle to left
                if(k-1>-1):
                    if(ball_color[x][k]=='temp' and ball_color[x][k-1]==turn
                    )or(ball_color[x][k]==ball_color[x][k-1]==turn
                    )or(ball_color[x][k]==turn and ball_color[x][k-1]=='e'
                    )or(ball_color[x][k]==ball_color[x][k-1]=='e'):
                        break
                    if(ball_color[x][k]==output1)and(ball_color[x][k-1]==output2):
                        count_illegal+=1
                        Reversing_Process(list_output, 4, y-1,k-1,-1, 0,0,0)
                        break

        if(0<=x<=6)and(0<=y<=6):
            l1,l2=x,y
            while(l1!=7 and l2!=7): # middle to downright
                if(ball_color[l1][l2]=='temp' and ball_color[l1+1][l2+1]==turn
                )or(ball_color[l1][l2]==ball_color[l1+1][l2+1]==turn
                )or(ball_color[l1][l2]==turn and ball_color[l1+1][l2+1]=='e'
                )or(ball_color[l1][l2]==ball_color[l1+1][l2+1]=='e'):
                    break
                if(ball_color[l1][l2]==output1)and(ball_color[l1+1][l2+1]==output2):
                    Reversing_Process(list_output, 5, x+1,l1+1,1, y+1,l2+1,1)
                    count_illegal+=1
                    break
                l1+=1
                l2+=1
        if(1<=x<=7)and(1<=y<=7):
            l1,l2=x,y
            while(l1!=0 and l2!=0): # middle to upleft
                if(ball_color[l1][l2]=='temp' and ball_color[l1-1][l2-1]==turn
                )or(ball_color[l1][l2]==ball_color[l1-1][l2-1]==turn
                )or(ball_color[l1][l2]==turn and ball_color[l1-1][l2-1]=='e'
                )or(ball_color[l1][l2]==ball_color[l1-1][l2-1]=='e'):
                    break
                if(ball_color[l1][l2]==output1)and(ball_color[l1-1][l2-1]==output2):
                    Reversing_Process(list_output, 6, x-1,l1-1,-1, y-1,l2-1,-1)
                    count_illegal+=1
                    break
                l1-=1
                l2-=1

        if(0<=x<=6)and(1<=y<=7):
            l1,l2=x,y
            while(l1!=7 and l2!=0): # middle to downleft
                if(ball_color[l1][l2]=='temp' and ball_color[l1+1][l2-1]==turn
                )or(ball_color[l1][l2]==ball_color[l1+1][l2-1]==turn
                )or(ball_color[l1][l2]==turn and ball_color[l1+1][l2-1]=='e'
                )or(ball_color[l1][l2]==ball_color[l1+1][l2-1]=='e'):
                    break
                if(ball_color[l1][l2]==output1)and(ball_color[l1+1][l2-1]==output2):
                    Reversing_Process(list_output, 7, x+1,l1+1,1, y-1,l2-1,-1)
                    count_illegal+=1
                    break
                l1+=1
                l2-=1
        if(1<=x<=7)and(0<=y<=6):
            l1,l2=x,y
            while(l1!=0 and l2!=7): # middle to upright
                if(ball_color[l1][l2]=='temp' and ball_color[l1-1][l2+1]==turn
                )or(ball_color[l1][l2]==ball_color[l1-1][l2+1]==turn
                )or(ball_color[l1][l2]==turn and ball_color[l1-1][l2+1]=='e'
                )or(ball_color[l1][l2]==ball_color[l1-1][l2+1]=='e'):
                    break
                if(ball_color[l1][l2]==output1)and(ball_color[l1-1][l2+1]==output2):
                    Reversing_Process(list_output, 8, x-1,l1-1,-1, y+1,l2+1,1)
                    count_illegal+=1
                    break
                l1-=1
                l2+=1

# Option 1 in get_option for Reversing Process
def Reversing_Process(coor1:list, part:int, start1,stop1,step1, start2,stop2,step2):
    global turnB
    x1,y1=coor1[0][0],coor1[0][1]
    checking=True
    list_option1=[]
    # dilihat apakah benar di dalam list reversi atau tidak
    if(part<=4):
        for i in range(start1,stop1,step1):
            if(0<=i<=7 and 0<=x1<=7 and 0<=y1<=7):
                if(part==1)or(part==2):
                    list_option1.append([i,y1])
                elif(part==3)or(part==4):
                    list_option1.append([x1,i])
    else:
        while(start1!=stop1)and(start2!=stop2):
            if(0<=start1<=7 and 0<=start2<=7):
                list_option1.append([start1,start2])
            start1+=step1
            start2+=step2

    # di-check apakah diantara titik tersebut ada empty/'e'
    for i in range(len(list_option1)):
        if(ball_color[list_option1[i][0]][list_option1[i][1]]=='e'):
            checking=False
    if(checking==True):
        for i in range(len(list_option1)):
            ball_color[list_option1[i][0]][list_option1[i][1]]='temp'

    # temp dalam list akan dirubah sesuai dengan color turnnya (black or white)
    if(turnB==True):n='b'
    else:n='w'
    for i in range(8):
        for j in range(8):
            if(ball_color[i][j]=='temp'):
                ball_color[i][j]=n

    # To print The new reversi
    for i in range(8):
        for j in range(8):
            if(ball_color[i][j]=='b'):
                black.stamp()
                black.goto((j * 50.25) - 175,  (-i * 50)  + 175)
            if(ball_color[i][j]=='w'):
                white.stamp()
                white.goto((j * 50.25) - 175,  (-i * 50)  + 175)
# Penyimpanan koordinat
def click_coor(x,y):
    global turnB,notYETclick
    time.sleep(0.2)
    # dilihat apakah titik coordinat yang telah diclick di dalam salah satu list 8x8
    # dan sesuai dengan green navigation nya
    yborder=200
    for vertical in range(8):
        xborder=-200
        for horizontal in range(8):
            if(xborder<x<=xborder+49.7 and yborder>y>=yborder-50) and (temp_list_black[vertical][horizontal]=='s'
            )or(xborder<x<=xborder+49.7 and yborder>y>=yborder-50) and (temp_list_white[vertical][horizontal]=='s'):
                ball_color[vertical][horizontal]="temp"
                notYETclick=False
                # lalu melakukkan reverse diantara titik2 yang memenuhi condition
                if(turnB==True):get_legal_reverse([[vertical,horizontal]], 'w','b','b')
                elif(turnB==False):get_legal_reverse([[vertical,horizontal]], 'b','w','w')

                
            xborder+=50
        yborder-=50

# Main Program
def MainProgram(side_turn:list,color):
    global temp_list_white, temp_list_black
    global list_black,turnB,notYETclick
    # merubah titik empty menjadi green dalam list sesuai dengan selection yang didapatkan
    for i in range(len(side_turn)):
        if(color=='b'):
            temp_list_black[side_turn[i][0]][side_turn[i][1]]='s'
        elif(color=='w'):
            temp_list_white[side_turn[i][0]][side_turn[i][1]]='s'


    # Agar dapat bisa melakukan click dalam turtle dan disimpan dalam procedure(def)
    turtle.onscreenclick(click_coor)

    # Sesuai turn... Jika sudah melakukan click dan turn player selanjutnya tidak 0 maka pergantian akan dilakukan
    if (turnB==True)and(notYETclick==False)and(list_white!=0):
        turnB=False
    elif (turnB==False)and(notYETclick==False)and(list_black!=0):
        turnB=True
#########################################################
#########################################################
# Bagian Board Game
borderline("square",0,0,'gold',20.5,20.5,10) # kotak gold luar
n=200
for _ in range(9):
    borderline("square",n,0,'black',20,0.05,1) # garis vertical
    borderline("square",0,n,'black',0.05,20,1) # garis horizontal
    n-=50

# bundaran player kecil di score atas dan persegi panjang tengah sebagai pemisah
borderline("square",0,280,'gold',4,0.1,2)
borderline("circle",-60,282,'black',2,2,2)
borderline("circle",59,282,'white',2,2,2)

# score awal
scorePlayer1,scorePlayer2=2,2

# List Reversi(8x8) dan reversi&green awal
ball_color=[['e' for _ in range(8)]for _ in range(8)]
ball_color[3][3],ball_color[4][4] = 'w','w'
ball_color[3][4],ball_color[4][3] = 'b','b'

# Turtle score 1
titleScore1 = turtle.Turtle()
titleScore1.shape()
titleScore1.color('black')
titleScore1.penup()
titleScore1.hideturtle()
titleScore1.goto(-120,270)
titleScore1.write(f"Player1        {scorePlayer1}", align="center", font=("timesnewroman", 16, 'bold'))

# Turtle score 2
titleScore2 = turtle.Turtle()
titleScore2.shape()
titleScore2.color('white')
titleScore2.penup()
titleScore2.hideturtle()
titleScore2.goto(120,270)
titleScore2.write(f"{scorePlayer2}        Player2", align="center", font=("timesnewroman", 16, 'normal'))


# Turtle untuk menaruh reversi sesuai warna...black/white/green(for navigation)
black = turtle.Turtle()
black.shape('circle')
black.color('black')
black.shapesize(2,2,1)
black.penup()
black.goto((3 * 50.25) - 175,  (-4 * 50)  + 175)
black.stamp()
black.goto((4 * 50.25) - 175,  (-3 * 50)  + 175)
black.stamp()

white = turtle.Turtle()
white.shape('circle')
white.color('white')
white.shapesize(2,2,1)
white.penup()
white.goto((3 * 50.25) - 175,  (-3 * 50)  + 175)
white.stamp()
white.goto((4 * 50.25) - 175,  (-4 * 50)  + 175)
white.stamp()

green = turtle.Turtle()
green.shape('circle')
green.color('springgreen')
green.shapesize(0.7,0.7,1)
green.penup()

# Turtle untuk Menunjukkan saat ini turn siapa
playerturn=turtle.Turtle()
playerturn.shape()
playerturn.color('black')
playerturn.hideturtle()
playerturn.penup()
playerturn.goto(-150,240)
playerturn.write(f"Black turn", align="center", font=("arial", 16, 'bold'))

# Making The Program Running
turnB=True
run=True
notYETclick=True
count_illegal=0
while(run==True):
    # mengecheck apakah sudah melakukan click atau belum
    notYETclick=True
    # list kosong untuk pin black dan pin white dan green selection
    list_black=[]
    list_white=[]
    wn.update()
    
    # Menunjukkan saat ini turn siapa
    if(turnB==True):
        playerturn.clear()
        playerturn.color('black')
        playerturn.goto(-150,240)
        playerturn.write(f"Black turn", align="center", font=("arial", 16, 'bold'))
    elif(turnB==False):
        playerturn.clear()
        playerturn.color('white')
        playerturn.goto(150,240)
        playerturn.write(f"White turn", align="center", font=("arial", 16, 'bold'))

    # memanggil procedure score untuk menghitung dan membuat tulisan papan score
    scorePlayer1,scorePlayer2=totalscore_pin()
    titleScore1.clear()
    titleScore1.write(f"Player1        {scorePlayer1}", align="center", font=("timesnewroman", 16, 'bold'))
    titleScore2.clear()
    titleScore2.write(f"{scorePlayer2}        Player2", align="center", font=("timesnewroman", 16, 'bold'))

    # copy ulang setiap while dijalankan
    temp_list_black= deepcopy(ball_color)
    temp_list_white= deepcopy(ball_color)

    # sesuai turn... sampai melakukkan click dan sesudah itu maka akan dipastikan dari 8 arah
    # dan melakukan reverse color sesuai condition
    if(turnB==True): # Black Turn
        MainProgram(Check_green_navigation(list_black,'w','e','b'),'b')
        # remove the previously green navigation
        green.clearstamps()
    elif(turnB==False): # White Turn
        MainProgram(Check_green_navigation(list_white,'b','e','w'),'w')
        # remove the previously green navigation
        green.clearstamps()

    # print the new green navigation
    for i in range(8):
        for j in range(8):
            if(temp_list_black[i][j]=='s'):
                green.stamp()
                green.goto((j * 50.25) - 175,  (-i * 50)  + 175)
            if(temp_list_white[i][j]=='s'):
                green.stamp()
                green.goto((j * 50.25) - 175,  (-i * 50)  + 175)
    if(count_illegal==-1):
        count_illegal=0
        if(turnB==True):
            print('Black Move is Zero')
            turnB=False
        else:
            print('White Move is Zero')
            turnB=True
    if(scorePlayer1+scorePlayer2==64):
        run=False

# The Final Score in Terminal
if(scorePlayer1>scorePlayer2):
    first=scorePlayer1
    player1st='Black'
    second=scorePlayer2
    player2st='white'
else:
    first=scorePlayer2
    player1st='white'
    second=scorePlayer1
    player2st='Black'

print(f"{'-'*50}")
print(f"{'|'}{'(` v `)/   ~ REVERSI FINAL SCORE ~   (` v `)/':^48}{'|'}")
print(f"{'-'*50}")
print(f"{'-'*50}")
print(f"{'|'}{'~ 1st RANK ~':^48}{'|'}")
print(f"{'- '*25}")
print(f"{'|'}{f'{player1st}    {first}':^48}{'|'}")
print(f"{'-'*50}")
print(f"{'-'*50}")
print(f"{'|'}{'~ 2nd RANK ~':^48}{'|'}")
print(f"{'- '*25}")
print(f"{'|'}{f'{player2st}    {second}':^48}{'|'}")
print(f"{'-'*50}")