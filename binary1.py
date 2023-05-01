a=[]
n=int(input("Enter the size of the array"))
for i in range(n-0):
    x=int(input("Enter the number"))
    a.append(x)
for i in range(n-0):
    for j in range(n-i-1):
        if (a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print("Sorted elements")
for j in range(n-0):
    print(a[j])
