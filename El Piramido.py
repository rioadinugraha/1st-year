row = int(input("number of rows: "))
num = 1
while (num<row+1):
    print("*" * num);
    num = num + 1;

row = int(input("number of rows: "))
num = 1
while (num<row+1):
    print(" "* (row - num) + "*" * num);
    num = num + 1;

row = int(input("number of rows: "))
num = 1
while (num<row+1):
    print(" "* (row - num) + "*" * num + "*" * (num-1));
    num = num + 1;
