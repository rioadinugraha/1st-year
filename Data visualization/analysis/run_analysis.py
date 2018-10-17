import sys

for n in sys.argv[1:]:
    print(n) #print out the filename we are currently processing
    input = open(n, "r")
    output = open(n + ".out", "w")
