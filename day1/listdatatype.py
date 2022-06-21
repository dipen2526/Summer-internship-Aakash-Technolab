#list datatype
list1 = [10,20,30,"akash",40,50,"Technolabs",60]

print("list1[2] = ",list1[2])
print("list1[0:3] = ",list1[0:3])
print("list1[5:] = ",list1[5:])

#take value from the user
#creating an empty list
lst=[]
#number of elements as input
n=int(input("Enter number of elements :"))
#iterating till the range
for i in range(0,n):
    ele = input("Enter value : ")

    lst.append(ele) #adding the element
print(lst)