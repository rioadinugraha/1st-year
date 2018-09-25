def Encryptor(string,Rot):
    Lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    Upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    Encrypt = {}
    Decrypt = {}
    index = 0
    string= list(string)
    for i in range(0, len(Lower)):
        index = i+Rot
        if index > (len(Lower)-1):
            index = index - 26
            Encrypt.update({Lower[i]:Lower[index]})
            Decrypt.update({Lower[index]:Lower[i]})
        else:
            Encrypt.update({Lower[i]:Lower[index]})
            Decrypt.update({Lower[index]:Lower[i]})
    index = 0
    for i in range(0, len(Upper)):
        index = i+Rot
        if index > (len(Upper)-1):
            index = index - 26
            Encrypt.update({Upper[i]:Upper[index]})
            Decrypt.update({Upper[index]:Upper[i]})
        else:
            Encrypt.update({Upper[i]:Upper[index]})
            Decrypt.update({Upper[index]:Upper[i]})
    Cypher = 0
    i = 0
    temp = ""
    for i in range(0,len(string)):
        if string[i] == " ":
            continue
        else:
            Cypher = Encrypt.get(string[i])
            string[i] = Cypher
    print(temp.join(string))

def Decryptor(string,Rot):
    Lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    Upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    Encrypt = {}
    Decrypt = {}
    index = 0
    string= list(string)
    for i in range(0, len(Lower)):
        index = i+Rot
        if index > (len(Lower)-1):
            index = index - 26
            Encrypt.update({Lower[i]:Lower[index]})
            Decrypt.update({Lower[index]:Lower[i]})
        else:
            Encrypt.update({Lower[i]:Lower[index]})
            Decrypt.update({Lower[index]:Lower[i]})
    index = 0
    for i in range(0, len(Upper)):
        index = i+Rot
        if index > (len(Upper)-1):
            index = index - 26
            Encrypt.update({Upper[i]:Upper[index]})
            Decrypt.update({Upper[index]:Upper[i]})
        else:
            Encrypt.update({Upper[i]:Upper[index]})
            Decrypt.update({Upper[index]:Upper[i]})
    Cypher = 0
    i = 0
    temp = ""
    for i in range(0,len(string)):
        if string[i] == " ":
            continue
        else:
            Cypher = Decrypt.get(string[i])
            string[i] = Cypher
    print(temp.join(string))


Choose = int(input("type 1 for encryption, type 2 for decryption"))
string = str(input("type down a string to Encrypt or decrypt"))
rot = int(input("please type the number of rotations "))
rot = rot % 26
if Choose == 1:
    Encryptor(string,rot)
elif Choose == 2:
    Decryptor(string,rot)

