#made without watching tutorial and i cooked 
#if you have any idea what's worng in this please send a pull request 


'''

import random

def Encrypt(word):
    
    if len(word) <= 2:
        return word[::-1]
    
    else:
        obj = word[1:]
        obj = obj + word[0]
        set = ""
        
        for i in range(0,3):
            click = random.randrange(0,2)
            if click==0:
                set = set+chr(random.randrange(97,122))
            else:
                set = set+chr(random.randrange(65, 90))
        
        obj = set+obj

        set2 = ""

        for j in range(0,3):
            click = random.randrange(0,2)
            if click==0:
                set2 = set2+chr(random.randrange(97,122))
            else:
                set2 = set2+chr(random.randrange(65, 90))
        
        obj = obj+set
    
    return obj
        

def Decrypt(word):
    obj2=""
    ans=""
    if len(word) <= 2:
        return word[::-1]
    
    else:
        obj2 = word[3:len(word)-3]
        ans = obj2[len(obj2)-1] + obj2[0:len(obj2)-1]
    
    return ans


try:
    Choice = int(input("DO YOU WANT TO ENCRYPT(1) OR DECRYPT(2) A MESSAGE?: "))
    if (Choice!=1 and Choice!=2):
        raise IndexError
    
except ValueError:
    print("INCORRECT VALUE ENTERED, YOU IMBECILE!")
except IndexError:
    print("ENTER A VALUE 0 OR 1, IDIOT!")


if Choice == 1:
    key = input("ENTER KEY: ")

    if key == "RevUp":
        Message = input("ENTER YOUR MESSAGE: ")
    else:
        print("GUESS YOU DON'T HAVE ACCESS!")
    
    words = Message.split()
    final = ""

    for i in range(len(words)):
        final = final + Encrypt(words[i]) + " "
    
    print(final)

elif Choice == 2:
    key = input("ENTER KEY: ")

    if key == "RevUp":
        Message = input("ENTER YOUR MESSAGE: ")
    else:
        print("GUESS YOU DON'T HAVE ACCESS!")

    words = Message.split()
    final = ""

    for i in range(len(words)):
        final = final + Decrypt(words[i]) + " "
    
    print(final)
'''