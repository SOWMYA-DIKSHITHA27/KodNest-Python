#calculate sum of all the consecutive numbers in the taken input
n=int(input())
total=0
counter=1
while counter<=n:
     total=total+counter
     counter+=1
print(f"Total: {total}")
