#tuple datatype
tuple1 = (10,20,30,"Akash",40,50,"Technolabs",60)

print("tuple[2] = ",tuple1[2])
print("tuple1[0:3] = ",tuple1[0:3])
print("tuple1[5:] = ",tuple1[5:])

#creating an empty list
lst=[]
#number of elements as input
n=int(input("Enter number of elements :"))
#iterating till the range
for i in range(0,n):
    ele = input("Enter value : ")

    lst.append(ele) #adding the element
tupl=tuple(lst)
print(lst)
print(tupl)