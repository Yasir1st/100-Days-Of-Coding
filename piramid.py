# num = int(input("Masukkan tinggi piramid : "))

# for i in range(1,num+1):
#     for j in range(1,num-i+1):
#         print(end=" ")
#     for j in range(i,0,-1):
#         print(j,end="")
#     for j in range(2,i+1):
#         print(j,end="")
#     print()

def pyramid(rows):
    for i in range(rows):
        if(i%2==0):
            print(' '*(rows-i-1)+'* '*(i+1))
        else:
            continue
    for j in range(rows-1,0,-1):
        if(j%2!=0):
            print(' '*(rows-j)+'* '*j)
        else:
            continue
pyramid(5)