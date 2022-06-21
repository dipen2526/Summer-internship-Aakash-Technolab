#dictionary datatype
d = {1: 'Akash', 2: 'technolabs', 'key':10}
print(type(d))
print("d[1] = ",d[1])
print("d[2] = ",d[2])
print("d['key'] = ",d['key'])

#take values from the user
m1={}
n = int(input("enter the number of ele :"))

for i in range(0,n):
    a,b = input("Enter key value pair data:").split()
    m1[a] = [b]
print(m1)
    