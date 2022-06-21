#while loop statement
i = 0

while i<5:
    print ("value of i : ",i)
    i += 1

#for loop statement
for i in 'Hello' :
    print('value : ',i)

#range function
for x in range(5):
    print("First range : ",x)

for y in range(3,6):
    print("Second range : ",y)

for z in range(1,5,2):
    print("Third range : ",z)

#loop with else
list1 =[10,15,"hello",20]

for i in range(len(list1)):
    print("value is :",list1[i])
else:
    print("no elements left.")
