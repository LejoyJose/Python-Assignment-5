terms=int(input())
a=0
b=1
sum=0

while sum< terms:
    print(a,end="")
    result=a+b
    a=b
    b=result
    sum+=1

