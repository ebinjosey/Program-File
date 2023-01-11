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
        

    

