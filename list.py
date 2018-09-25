# 1.	Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

def max_of_three(a,b,c):
    list = [a,b,c]
    list.sort()
    return list[2]
#print(max_of_three(2,9,4))


# 2.	Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
def length(c):
    total = 0
    i = 0
    for i in c:
        total += 1
    print("length of set " + str(total))

# 3.	Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

def vowel(a):
    a.lower()
    if a== "a" or a== "i" or a== "u" or  a== "o" or a== "e":
        return True
    else:
        return False
#print(vowel("I"))

# 4.Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".

def reverse(a):
    a = a[::-1]
    print(a)

# 5.Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)
def is_member(x,a):
    for i in a:
        if i == x:
            print("True")
            break
    else:
        print("False")


#6.	Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.

def overlapping(first,second):
    i=0
    j=0
    k = 0
    while i<len(first):
        while j <len(second):
            if first[i] == second[j]:
                print("True")
                k = 1
                break
            j=j+1
        i=i+1
        j= 0
    if k == 0:
        print("false")

# 7.7.	Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx". (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx". For the sake of the exercise you should ignore that the problem can be solved in this manner.)
def generate_n_chars(mult,chara):
    prnt = str()
    i=0
    for i in range (0,mult):
        prnt += chara
    print(prnt)


#8.

def histogram(k):
    i=0
    for i in range (0,len(k)):
        print("*"*k[i])
#9.

def wordLength(s):
    i=0
    list = []
    for i in range (0,len(s)):
        list.append(len(s[i]))
    print(list)

#wordLength(["ok","yo
# u","Boda"])

#10.
def maxWord(s):
    i=0
    list = []
    for i in range (0,len(s)):
        list.append(len(s[i]))
    list.sort()
    print(list[(len(list)-1)])

 #maxWord(["fhalsahdkjsahd","asdsadsa","zzzzzz"])

#11.
def pangram(text):
    text = text.lower()
    req =["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    sentence = text
    i=0
    j=0
    k = 0
    while i<len(req):
        while j <len(sentence):
            if req[i] == sentence[j]:
                k += 1
                break
            j=j+1
        i=i+1
        j= 0
    if k == 26:
        print("True")
    else:
        print("False")

#pangram("The quick brown fox jumps over the lazy dog")

12.
def make_ing_form(a):
    vowel = ["a","i","u","e","o"]
    i=0
    k = True
    for i in range (0,len(vowel)):
        if a[-1] == vowel[i]:
            k = False
        if a[-2] == vowel[i]:
            k = True
        if a[-3] == vowel[i]:
            k = False

    a = a.lower()
    if a[-1]== "e" and a[-2]=="i":
        a = a [:-2]
        a = a + "ying"
        print(a)

    elif a[-1]== "e":
        a = a[:-1]
        a = a + "ing"
        print(a)

    elif k == True:
        a = a + a[-1] + "ing"
        print(a)

    else:
        a = a + "ing"
        print(a)
#make_ing_form("hug")
