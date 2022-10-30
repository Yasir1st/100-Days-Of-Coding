simbol="8"
print(" ")
def ya():
    for row in range(1,15):
        for col in range(1,93):
            #huruf y
            if(row==1 and col<=5):
                print(simbol,end="")
            elif(row==1 and col>=13 and col<=17):
                print(simbol,end="")
            elif(col-row==0 and row<=7):
                print(simbol,end="")
            elif(col-row==4 and row<=5):
                print(simbol,end="")
            elif(col+row==18 and row<=7):
                print(simbol,end="")
            elif(col+row==14 and row<=5):
                print(simbol,end="")
            elif(row==14 and col>=7 and col<=11):
                print(simbol,end="")
            elif(col==7 and row>=8):
                print(simbol,end="")
            elif(col==11 and row>=8):
                print(simbol,end="")

            #huruf a
            elif(row==1 and col>=20 and col<=24):
                print(simbol,end="")
            elif(row==4 and col>=21 and col<=23):
                print(simbol,end="")
            elif(row==7 and col>=18 and col<=26):
                print(simbol,end="")
            elif(row==9 and col>=18 and col<=26):
                print(simbol,end="")
            elif(col+row==21 and row<=7):
                print(simbol,end="")
            elif(col+row==25 and row<=7 and row>=4):
                print(simbol,end="")
            elif(col-row==23 and row<=7):
                print(simbol,end="")
            elif(col-row==19 and row<=7 and row>=4):
                print(simbol,end="")
            elif(col==14 and row>=8):
                print(simbol,end="")
            elif(col==18 and row>=10):
                print(simbol,end="")
            elif(col==30 and row>=8):
                print(simbol,end="")
            elif(col==26 and row>=10):
                print(simbol,end="")
            elif(row==14 and col>=14 and col<=18):
                print(simbol,end="")
            elif(row==14 and col>=26 and col<=30):
                print(simbol,end="")

            #huruf s
            elif(row==1 and col>=37 and col<=66):
                print(simbol,end="")
            elif(row==3 and col>=39 and col<=64):
                print(simbol,end="")
            elif(row==7 and col>=36 and col<=66):
                print(simbol,end="")
            elif(row==9 and col>=33 and col<=63):
                print(simbol,end="")
            elif(row==12 and col>=35 and col<=60):
                print(simbol,end="")
            elif(row==14 and col>=33 and col<=62):
                print(simbol,end="")

            elif(col==33 and row>=5 and row<=9):
                print(simbol,end="")
            elif(col==66 and row>=7 and row<=10):
                print(simbol,end="")
            elif(col+row==47 and row>=12):
                print(simbol,end="")
            elif(col+row==38 and row<=5):
                print(simbol,end="")
            elif(col+row==67 and row<=3):
                print(simbol,end="")
            elif(col+row==42 and row>=3 and row<=6):
                print(simbol,end="")
            elif(col+row==72 and row>=9 and row<=12):
                print(simbol,end="")
            elif(col+row==76 and row>=10):
                print(simbol,end="")
            
            elif(col+row==55 and row>=9 and row<=12):
                print(simbol,end="")
            elif(col+row==60 and row>=9 and row<=12):
                print(simbol,end="")
            elif(col+row==54 and row>=3 and row<=7):
                print(simbol,end="")
            elif(col+row==59 and row>=3 and row<=7):
                print(simbol,end="")

            #huruf i
            elif(row==1 and col>=69 and col<=73):
                print(simbol,end="")
            elif(row==14 and col>=69 and col<=73):
                print(simbol,end="")
            elif(col==69 or col==73):
                print(simbol,end="")

            #huruf r
            elif(row==1 and col>=76 and col<=90):
                print(simbol,end="")
            elif(row==3 and col>=80 and col<=86):
                print(simbol,end="")
            elif(row==7  and col>=80 and col<=86):
                print(simbol,end="")
            elif(row==9  and col>=80 and col<=86):
                print(simbol,end="")
            elif(row==14  and col>=76 and col<=80):
                print(simbol,end="")
            elif(row==14  and col>=88 and col<=92):
                print(simbol,end="")

            elif(col==76):
                print(simbol,end="")
            elif(col==80 and row>=3 and row<=7):
                print(simbol,end="")
            elif(col==80 and row>=9 and row<=14):
                print(simbol,end="")  
            elif(col==88 and row>=11):
                print(simbol,end="")
            elif(col==92 and row>=11):
                print(simbol,end="")
            elif(col==92 and row>=3 and row<=7):
                print(simbol,end="")
            elif(col+row==93 and row>=5 and row<=7):
                print(simbol,end="")
            elif(col+row==99 and row>=7 and row<=9):
                print(simbol,end="")
            elif(col-row==89 and row<=3):
                print(simbol,end="")
            elif(col-row==83 and row>=3 and row<=5):
                print(simbol,end="")
            elif(col-row==77 and row>=9 and row<=11):
                print(simbol,end="")
            elif(col-row==81 and row>=9 and row<=11):
                print(simbol,end="")

            else:
                print(end=" ")
        print()   

ya()
print(" ")

 