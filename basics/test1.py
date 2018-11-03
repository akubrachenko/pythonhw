import random
#question 1
def q1(arg1):
    print("Hello," +arg1 + "!")
q1("World")
#end
#question 2
def sum(arg1):
    newarg1 = 0
    for i in arg1:
        newarg1 += i
    return newarg1
print (sum([1,2,3,4]))
def multiply(arg2):
    newarg2 = 1
    for i in arg2:
        newarg2 *= i
    return newarg2
print (multiply([1,2,3,4]))
#end
#question3
def reverse(arg1):
    return arg1[::-1]
print(reverse("I am testing"))
#end
#question 4
def isPalindrome(arg1):
    if arg1 == arg1[::-1]:
        return "True"
    else: 
        return "False"
print(isPalindrome("rararte"))
#end
#question 5
def histogram(arg):
    for i in arg:
        print (i*"*")
histogram([4,9,7])
#end
#question 6
def caesarCipher(s,k):
    alphabet = ("a", "b", "b", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ",", ".", "!", "?")
    i=0
    news =""
    for i in range(len(s)):
        index_l = alphabet.index(s[i]) #index of l in alphabet
        if index_l + k > 30: index_a =index_l + k - 30
        else: index_a = index_l + k
        news = news+alphabet[index_a]
        i += 1
    print(news)
caesarCipher("test", 2)
def fakeCaesarCipher(s,k):
    newstr = ""
    i=0
    l=len(s)
    for i in range(l):
        newstr += chr(ord(s[i]) + k)
    print(newstr)
fakeCaesarCipher("I am grut", 5) 
#end
#question 7
def diagonalReverse(matrix):
    i = 0
    j = 0
    newmatrix = []
    for i in range(len(matrix)):
        arr = []
        for j in range(len(matrix[i])):
            arr.append(matrix[j][i])
        newmatrix.append(arr)
    return newmatrix
print(diagonalReverse(matrix = [[1,2,3], [4,5,6], [7,8,9]]))
#end
#question 8
def game(arg1, arg2):
    lacky_number = random.randrange(arg1, arg2)
    flag = True
    while flag:
        user_number = int(input("Please enter number: "))
        if lacky_number != user_number: print("Try again!")
        else: 
            print("Congratulation, you are lacky man!")
            flag = False
#game(1, 2)
#end
def balance(str1):
    l = len(str1)
    i=0
    count = 0
    for i in range(l):
        if count < 0: break
        if str1[i] == "[": count +=1
        elif str1[i] == "]": count -=1
    if count > 0 or count < 0: print(str1 + "NOT OK")
    else: print(str1 + "OK")
balance("[][][][][]]]][[[[]")
#end
#question 10
def charFreq(str1):
    i=0
    j=0
    l=len(str1)
    count = 0
    newstr = ""
    dic = {}
    for i in range(l):
        for j in range(l):
            if str1[j] == str1[i]:
                count += 1
                newstr = str1[i]
        dic[newstr] = str(count) 
        count = 0
    print(dic)
charFreq("aaabbbbjajjjewpoiu")
#end
#question 11
def decToBin(num):
    binary = ""
    while num !=0:
        if num % 2 == 0: binary += "0"
        else: binary += "1"
        num = num // 2
    print(binary)
decToBin(6)
#end            
                 
            
            
