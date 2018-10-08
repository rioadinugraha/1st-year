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


def main():
    numbers=[]
    status = "y"
    while status.upper() != "N":
        numbers.append(int(input("please input an integer")))
        status = str(input("do you want to continue? Y/N"))
    print(sorting(numbers))

main()
