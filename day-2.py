#ASSIGNMENT - 2
#QUESTION - 1
list1=[]
for i in range(10):
    inp = int(input("Enter the number:"))
    even_num = inp%2
    if even_num==0:
        list1.append(inp)
print(list1)

#QUESTION - 2
print("\nQuestion - 2")
list_comp = []
for letter in 'human':
    list_comp.append(letter)
print(list_comp)

#QUESTION - 3
print("\nQuestion - 3")
d = {}
n = int(input())
for i in range(1,n+1):
    dic_data = i*i
    d[i] = dic_data
print(d)

#QUESTION - 4
import math
print("\nQuestion - 4")
up=0
down=0
left=0
right=0
n = int(input())
for i in range(1,n+1):
    if i==1:
        up=int(input("UP "))
    elif i==2:
        down=int(input("DOWN "))
    elif i==3:
        left=int(input("LEFT "))
    elif i==4:
        right=int(input("RIGHT "))
    else:
        print("four direction only available")
        break
x=(right-left)*(right-left)
y=(up-down)*(up-down)
d = x+y
d=math.sqrt(d)
d=round(d)
print("\n",d)

