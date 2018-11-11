import random
#question 1
def q1(arg1):
    return("Hello," +arg1 + "!")
#question 2
def sum(arg1):
    newarg1 = 0
    for i in arg1:
        newarg1 += i
    return newarg1
def multiply(arg2):
    newarg2 = 1
    for i in arg2:
        newarg2 *= i
    return newarg2
multiply([1,2,3,4])
#end
#question3
def reverse(arg1):
    return arg1[::-1]
reverse("I am testing")
#end
#question 4
def isPalindrome(arg1):
    if arg1 == arg1[::-1]:
        return "True"
    else: 
        return "False"
isPalindrome("rararte")
#end
#question 5
def histogram(arg):
    histogram = []
    for i in arg:
        histogram.append(i*"*")
    return histogram
histogram([4,9,7])
#end
#question 6
def CaesarCipher(s,k):
    newstr = ""
    i=0
    l=len(s)
    for i in range(l):
        newstr += chr(ord(s[i]) + k)
    return newstr
CaesarCipher("I am grut", 5) 
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
diagonalReverse(matrix = [[1,2,3], [4,5,6], [7,8,9]])
#end
#question 8
def game(arg1, arg2):
    lacky_number = random.randrange(arg1, arg2)
    flag = True
    while flag:
        user_number = int(input("Please enter number: "))
        if lacky_number != user_number: print("Try again!")
        else: 
            #print("Congratulation, you are lacky man!")
            flag = False
            return True
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
    if count > 0 or count < 0: 
        #print(str1 + "NOT OK")
        return False
    else: 
        #print(str1 + "OK")
        return True
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
    return dic
charFreq("aaabbbbjajjjewpoiu")
#end
#question 11
def decToBin(num):
    binary = ""
    while num !=0:
        if num % 2 == 0: binary += "0"
        else: binary += "1"
        num = num // 2
    return binary
decToBin(6)
#end            
                 
            
            
