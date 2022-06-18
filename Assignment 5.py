#Q1
print()
string = str(input("Enter the string to be printed in reverse order :\n")) 
string1 = string[::-1]

print()

print("The reversed order of string entered is :")
print(string1)
print()
#Q2
print()
range_1 = int(input("Enter the initial number of range :\n"))
print()
range_2 = int(input("Enter the last(ending) number of range :\n"))
print()
a = 1
number = int(input("Enter the divisor for entered range :\n"))

print()

print("Numbers divisile in the range are :")

for i in range(range_1,range_2):
    if i % number == 0:
        print(a,".",i)
        print()
    else:
        continue
    a = a + 1 
#Q3
import math

print()
side_1 = float(input("Enter the lenght of 1st side of triangle whose area is to be calculated :\n"))
print()
side_2 = float(input("Enter the lenght of 2nd side of triangle whose area is to be calculated :\n"))
print()
side_3 = float(input("Enter the lenght of 3rd side of triangle whose area is to be calculated :\n"))
print()

s = (side_1+side_2+side_3)/2

largest  = max(side_1,side_2,side_3)
if s > side_3 and s> side_1 and side_2 < s and largest < ((side_1 + side_2 + side_3) - largest):
    print("Area of triangle whose sides are entered is :" , 
    math.sqrt( s*(s-side_1)*(s-side_2)*(s-side_3) ))    
else:
    print("Triangle not possible")
print()
#Q4
i = 0
n = 0 
x = "*"
print()

while i <=9:
    while n <= 5:
        print(n*x)
        n = n + 1
        i = i + 1

    while i <= 9 : 
        print((n-2)*x)
        n = n - 1
        i = i + 1

print()
#Q5
n=int(input("enter no of rows to be printed:"))
a=0
for i in range (n):
    for j in range(i+1):
        print((chr(65+a)),end="")
        a=a+1
        while a>25:
            a=a-26
    print()        
#Q6
lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
#Q7
print("The numbers are divisible by only 7 not 11")
for i in range(1,500):
    if i % 7 == 0 and i % 11 != 0:
        print(i)

print("The numbers are only divisible by only 11 not 7")
for i in range(1,500):

    if i % 7 != 0 and i % 11 == 0:
        print(i)
        
print("The numbers are divisible by both 7 and 11")
for i in range(1,500):

    if i % 7 == 0 and i % 11 == 0:
        print(i)
#Q8
list_p = []
list_n = []
list_o = []
list_e = []

print()

num_1 =  int(input("Enter the 1st number to be checked :\n"))
num_2 =  int(input("Enter the 2nd number to be checked :\n"))
num_3 =  int(input("Enter the 3rd number to be checked :\n"))
num_4 =  int(input("Enter the 4th number to be checked :\n"))
num_5 =  int(input("Enter the 5th number to be checked :\n"))
num_6 =  int(input("Enter the 6th number to be checked :\n"))
num_7 =  int(input("Enter the 7th number to be checked :\n"))
num_8 =  int(input("Enter the 8th number to be checked :\n"))
num_9 =  int(input("Enter the 9th number to be checked :\n"))
num_10= int(input("Enter the 10th number to be checked :\n"))

list_all = [num_1,num_2,num_3,num_4,num_5,num_6,num_7,num_8,num_9,num_10]

print()

for i in list_all:
    if i >= 0 :
        print(i,"is a positive ", end = "")
        list_p.append(i)
    else:
        list_n.append(i)
        print(i,"is a negative ", end="")

    if i % 2 == 0:
        list_e.append(i)
        print("as well as even number.")
    else:
        list_o.append(i)
        print("as well as odd number")
    
    print()


print("The following input numbers are odd :\n",*list_o , sep = " , ")
print()
print("The following input numbers are positive :\n",*list_p , sep = " , ")
print()
print("The following input numbers are negative :\n",*list_n , sep = " , ")
print()
print("The following input numbers are even :\n",*list_e , sep = " , ")
print()

Number = int(input("Enter the number to be checked for number of appearences :\n"))

count_1 = list_all.count(Number)

print("The number appeared",count_1,"times.")
#Q9
str=input("enter a string:")
counts=dict()
words=str.split(' ')
for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
print(counts)        
            
    