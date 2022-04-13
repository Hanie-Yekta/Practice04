#meqdar ertefa nesf louzi
print("enter the height of the Rhombus:")
n=int(input())

#qesmat balaye louzi
for i in range(0,n):
    print(" "*(n-i),"*"*((2*i)-1))

#qesmat paein louzi
for j in range(n,-1,-1):
    print(" "*(n-j),"*"*((2*j)-1))