
# whatever = input(str("input text of whatever choice"))
# while whatever != "exit":
    # whatever = input(str("input exit to leave "))


# def spam ():
  #  eggs = 99
   # bacon()
    #print(eggs)

#def bacon():
 #   ham = 101
  #  eggs = 0
# spam()
#import key as key


#def palindrome(str):
 #   print(str[0::-1])
  #  print(str)
   # if str == str[::-1]:
    #    print("palindrome")
    #else:
     #   print("not palindrome")
#kk = input (str("Anything"))
#palindrome(kk)

#kk.sort(key=str.lower)
#print(kk)

mycat ={"size":"fat","color":"red","sound":"loud"}
#print(mycat)
#print(mycat['size'])

#a = ["a","b"]
#print(mycat["size"])


def countoccur(myinput):
    count = {}
    for character in myinput:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    print(count)


countoccur("i am soooooo sleepy")


allguests = {"hengky":{"beer": 0 ,"pizza":20},
             "nico":{"dimsum": 2, "lumpia": 1},
             "Rino":{"soda": 5, "chips": 10},
             "ikhsan":{"beer": 7, "chips": 5}}
def totalbrought(guests):
    count = {}
    for i in guests.keys():
        for j in guests[i].keys():
            count.setdefault(j,0)
            count[j] = count[j] + guests[i].get(j)

    print(count)


def totalBrought(guests,item):
    numBrought = 0
    for k,v in guests,items():
        numBrought = numBrought + v.get(item,0)
    return numBrought

print(totalBrought(allguests,beer))
Print("\""...............)

