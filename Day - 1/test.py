
ara = []
user = int(input())
for x in range(0,user):
    a = int(input())
    ara.append(a)
print(ara)
n = int(input())
count = 0
for i in ara:
    if(i==n):
        count = count + 1
if(count==0):
    print(n," is not present in ara")
else:
    print(n,"present in ara",count,"times")
