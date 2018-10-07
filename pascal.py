def pascal_triangle(n):
    print([1])
    print([1,1])
    pascal = [0,0,0]
    prevLine = [1,1]
    for k in range (3,n+1):
        for i in range(0,k):
            if i == 0:
                value = prevLine[i]
                pascal[i] = value
            elif i == k-1:
                value = 1
                pascal[i]= value
            else:
                value = prevLine[i] + prevLine[i-1]
                pascal[i] = value

        print(pascal)
        prevLine = list(pascal)
        pascal=[0]*(len(pascal)+1)
        prevLine.append(0)



pascal_triangle(6)
