n=int(input())
first=0
second=1

for i in range(n):
    temp=first
    first=second
    second=first+temp
    
print(temp)

