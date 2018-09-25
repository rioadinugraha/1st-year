def KMP(string):
    i= 0
    lista=str(string)
    start = 0
    abb= str()
    for i in range (0,len(lista)):
        if "-" == lista[i]:
            abb +=lista[start]
            start = i+1
        elif i==(len(lista)-1):
            abb += lista[start]
    print(abb)

KMP("Knuth-Morris-Pratt")

def Modul42(List):
    NewList=[]
    i= 0
    k=0
    for i in range (0,len(List)):
        k = List[i] % 42
        NewList.append(k)
    NewSet = set(NewList)
    print(len(NewSet))

Modul42([84,3,4,6,42,6,8])

def AliceNBob(N):
    mod= 0
    mod = N % 2
    if mod ==1:
        print ("Alice wins")
    else:
        print("Bob Wins")

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
    print((position.index(1)+1))
CupsNBall ("CBABCACCC")
