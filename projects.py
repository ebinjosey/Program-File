import math
import random

# To check if your number is a prime or composite

n = int(input("Enter your number"))

if n > 1:
    for i in range(2,n):
        if n%i==0:
            print("Your number is not a prime number.")
            break

        else:
            print("Your number is a prime number.")
            break

elif n == 0 or 1:
    print("Your number is neither prime nor composite")
    
# 8 WAP to generate fibonacci sequence

n = int(input("Enter no. of terms for Fibonacci sequence:"))
fibonacci=[]
a,b=0,1
for i in range(n):
    fibonacci.append(a)
    a,b=b,a+b

print("The first", n, "terms of the Fibonacci sequence are:", (fibonacci))


# 12 WAP to create user-input list and separate odd and even into separate lists 

lst = []
o = []
e = []

n=int(input("Enter the no. of elements:"))

for i in range(0,n):
    ele=int(input("Enter element:"))
    lst.append(ele)

for i in lst:
    if i%2==0:
        e.append(i)

    else:
        o.append(i)

print("Elements that are odd are:", o)
print("Elements that are even are:", e)

# 13 WAP to swap first and last elements of a list

lst=[]
n=int(input("Enter number of elements:"))

for i in range (0,n):
    ele=int(input("Enter your elements:"))
    lst.append(ele)

lst[0],lst[-1]=lst[-1],lst[0]

print(lst)

# 14 WAP to create user-input list and multiply odd elements by 3 and divide even elements by 2

lst=[]
o=[]
e=[]

n=int(input("Enter no. of elements:"))

for i in range(0,n):
    ele=int(input("Enter your elements:"))
    lst.append(ele)

for i in lst:
    if i%2==0:
        e.append(i/2)

    else:
        o.append(i*3)

print("Odd elements multipled by 3 are:",o)
print("Even elements divided by 2 are:",e)

# 15 WAP to create user-input list and display largest element in the list

lst=[]
n=int(input("Enter no. of elements:"))

for i in range(0,n):
    ele=int(input("Enter your elements:"))
    lst.append(ele)

lst.sort()
print("Largest element is:", lst[-1])


# 16 WAP to create user-input list and display mean of the list

lst=[]
n=int(input("Enter no. of elements:"))

for i in range(0,n):
    ele=int(input("Enter your elements:"))
    lst.append(ele)

print("The mean of the list is:", sum(lst)/len(lst))

# 17 WAP to implement linear search in user input list [needs work]

lst=[]
n=int(input("Enter no. of elements:"))

for i in range(0,n):
    ele=int(input("Enter your elements:"))
    lst.append(ele)

x = int(input("Enter number to search:"))
Found = False

for k in range(len(lst)):
    if lst[k] == x:
        Found = True
        print("Found at position:",k+1)
        break
    
    if(Found == False):
        print(x,"is not found in the list")
        
# 18 Packing and Unpacking of a Tuple

T1=(100,200,300)
a,b,c=T1
print(a)
print(b)
print(c)
print(T1)
    
# 19 Indirectly modifying Tuples
T1=(100,200,300)
a,b,c=T1
a=400
T1=a,b,c
print(T1)


#20 WAP to create tuple from user input string and user input list

string1=input("Enter your string that you want to convert into a tuple:")
tuple1=tuple(string1)

list2=list(input("Enter your list that you want to convert into a tuple:"))
tuple2=tuple(list2)

print(tuple1)
print(tuple2)
 
# 21 WAP to create user-input dictionary and print key, value pairs

mydict={}
n=int(input("Enter number of elements:"))
for i in range(0,n):
    a=input("Enter key:")
    b=input("Enter value:")
    mydict[a]=b
print(mydict)

tuple1=mydict.items()
for key,value in tuple1:
    print(key,value)
   
# 22 WAP to create user-input dictionary and check existence of a key

mydict={}
n=int(input("Enter number of elements:"))
for i in range(0,n):
    a=input("Enter key:")
    b=input("Enter value:")
    mydict[a]=b
print(mydict)

# 23 WAP to create user-input dictionary and delete last element
mydict={}
n=int(input("Enter number of elements:"))
for i in range(0,n):
    a=input("Enter key:")
    b=input("Enter value:")
    mydict[a]=b
print(mydict)

k,v=mydict.popitem()
print(k,v)

print(mydict)

# 24 WAP to create a menu driven dictionary with roll number, name, and marks of students and display the names of students who have scored marks above 75
d={}
n=int(input("Enter no. of students:"))
for i in range(0,n):
    a=int(input("Enter roll number:"))
    b=input("Enter name:")
    c=int(input("Enter marks:"))
    d[a]=[b,c]

print(d)
y=d.items()
print("People who scored more than 75 marks are:")
print("Name\t, Roll\t, Marks\t")
for i in y:
    k,v=i
    if v[1]>75:
        print(k,'\t', v[0], '\t', v[1])

# 25  WAP to create a menu driven dictionary for storing employee names and salary and access them

dic={}
name_lst=[]

while True:
    print('''Choose from the following:
1. Add Employee Details
2. Show all Employee Details
3. Search Employee
0. Quit''')

    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter name of your employee:")
        salary=int(input("Enter salary of your employee:"))
        dic.update({name:salary})
        name_lst.append(name)
        print('\n')

    elif choice==2:
        print("**********EMPLOYEE DETAILS**********")
        for i in range(len(name_lst)):
            print("Name:", name_lst)
            print("Salary:", dic[name_lst[i]])
            print('\n')

    elif choice==3:
        name_search=input("Enteer name of Employee to search:")
        print("Salary:", dic[name_search])
        print('\n')

    elif choice==0:
        break

    else:
        print("Invalid Choice")
        
# 26 WAP to create a menu driven dictionary for storing phonebook names and number and access them
        
phonebook={}
choice=1

while choice!=0:
    print('''Choose from the following:
1. Add a record
2. Show all records
3. Search record
4. Change a record
5. Delete a record
0. Quit''')

    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter name:")
        phone=int(input("Enter 6 digit phone number:"))
        if name in phonebook:
            print("Name already exists")
        else:
            phonebook[name]=phone
            print("Record Added")

    elif choice==2:
        print("**********PHONE DETAILS**********")
        for i in phonebook:
            print("Name:", i)
            print("Phone:", phonebook[i])
            print('\n')

    elif choice==3:
        name_search=input("Enter name of person to search:")
        print("Phone:", phonebook[name_search])
        print('\n')

    elif choice==4:
        name==input("Enter name:")
        if name in phonebook:
            phone=int(input("Enter new 6 digit number:"))
            print("Record Added")
        else:
            print("Record not found")
            

    elif choice==5:
        name=input("Enter name:")
        if name in phonebook:
            del phonebook[name]
            print("Record Deleted")
        else:
            print("Record not found")
        print('\n')


    elif choice==0:
        break

    else:
        print("Invalid Choice")
        
# 27 WAP to find the trigonometric functions of a user input angle in degrees

num=int(input("Enter the degree:"))
rad= math.radians(num)

print("The sin function of the given number is", math.sin(rad))
print("The cos function of the given number is", math.cos(rad))
print("The tan function of the given number is", math.tan(rad))
print("The sec function of the given number is", 1/math.cos(rad))
print("The cosec function of the given number is", 1/math.sin(rad))
print("The cot function of the given number is", 1/math.tan(rad))


# 28 WAP to generate random number between 1 to 100


randno = random.randint(1, 100)

for i in range(3):
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == randno:
        print("Congratulations! You guessed the number correctly.")
        break
    elif guess < randno:
        print("The number you guessed is too low.")
    else:
        print("The number you guessed is too high.")

if i == 2:
    print("You were unable to guess the number in the given tries. The correct number was", randno)


        



