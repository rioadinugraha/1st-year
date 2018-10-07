def sorting(list):
    i = 0
    while i+1 < len(list):
        if list[i+1]< list[i]:
            temp = list[i]
            list[i] = list [i+1]
            list[i+1] = temp
            i = 0
        else:
            i += 1
    return list


print(sorting([5,2,200,8,7,4,5,98,54,62]))
