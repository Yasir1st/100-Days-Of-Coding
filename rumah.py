print(" ")
bata ="$"
#atap
for row in range(1,8):
    for col in range(1,37):
        if row==7:
            print(bata,end="")
        elif(row+col==8 or col-row==6):
            print(bata,end="")
        elif(row==1 and col>=7 and col<=30 ):
            print(bata,end="")
        elif(row==7 and col<37 or col-row==29):
            print(bata,end="")
        else:
            print(end=" ")
    print()

#body
for row in range(1,8):
    for col in range(1,37):
        #pintu
        if row==7:
            print(bata,end="")
        elif(col==1 or col==36 or col==13):
            print(bata,end="")
        elif(col==5 and row>=2):
            print(bata,end="")
        elif(col==9 and row>=2):
            print(bata,end="")
        
        #jendela
        elif(row==2 and col>=5 and col<=9):
            print(bata,end="")
        elif(row==2 and col>=17 and col<=21):
            print(bata,end="")
        elif(row==2 and col>=26 and col<=30):
            print(bata,end="")
        elif(row==5 and col>=17 and col<=21):
            print(bata,end="")
        elif(row==5 and col>=26 and col<=30):
            print(bata,end="")
        elif(col==17 and row>=2 and row<=5):
            print(bata,end="")
        elif(col==21 and row>=2 and row<=5):
            print(bata,end="")
        elif(col==26 and row>=2 and row<=5):
            print(bata,end="")
        elif(col==30 and row>=2 and row<=5):
            print(bata,end="")
        else:
            print(end=" ")
    print()