def KMP(string):
    i= 0
    string=str(string)
    start = 0
    abbreviation = str()
    for i in range(0,len(string)):
        if "-" == string[i]:  # finds the "-" in the names
            abbreviation += string[start] # then gets the First letter of the the string passed by the loop
            start = i+1 # starts the next string sequence after the "-"
        elif i == (len(string)-1):   # this line checks if it's the last string
            abbreviation += string[start]
    return abbreviation

def Modul42(List):
    NewList=[]
    i= 0
    k=0
    for i in range (0,len(List)):
        k = List[i] % 42
        NewList.append(k)
    NewSet = set(NewList)
    return len(NewSet)
#Modul42([84,3,4,6,42,6,8])

def AliceNBob(N):
    mod= 0
    for i in range (0,len(N)):
        mod = N[i] % 2
        if mod ==1:
            print ( "No of rocks = " + str(N[i]) + ", Alice wins")
        else:
            print("No of rocks = " + str(N[i]) + ", Bob wins")

def CupsNBall(ballsequence):
    ballsequence = ballsequence.lower()
    i= 0
    position = [1,0,0]
    for i in range (0,len(ballsequence)):
        if ballsequence[i] == "a":
            position[0], position[1] = position[1], position [0]
        elif ballsequence[i] == "b":
            position[1], position[2] = position[2], position [1]
        elif ballsequence[i] == "c":
            position[2], position[0] = position[0], position [2]
    print("the ball is in cup no. "+ str((position.index(1)+1)) + " from the left")
#CupsNBall ("CBABCACCC")

while True:
    try:
        print("""
***************************************************
*       Which function do you want to use         *
*       1.KMP                                     *
*       2.Modul42                                 *
*       3.AliceNBob                               *
*       4.CupsNBall                               *
***************************************************""")
        module = int(input("Choice: "))
    except ValueError :
        print("non valid value detected please re-input")
    if module < 0 or module > 4:
        print("non valid integer detected please input correct values")
    elif module == None:
        print("please input a value")
    else:
        break

if module == 1:
    string = str(input("please type a string separated by hyphens to process "))
    print("The abbreviation is " + str(KMP(string)))
elif module == 2:
    list = [int(i) for i in input("please type numbers separated by spaces that you want checked").split()]
    print("the number of unique divisions by 42 is " + str(Modul42(list)))
elif module == 3:
    list = [int(i) for i in input("please type numbers separated by spaces for the number of rocks per round ").split()]
    AliceNBob(list)
elif module == 4:
    sequence = str(input("""please write a rotation sequence where 
\"a\" swaps glass 1 and 2 
\"b\" swaps glass 2 and 3
\"c\" swaps glass 3 and 1
invalid input will be disregarded 
sequence: """))
    CupsNBall(sequence)
