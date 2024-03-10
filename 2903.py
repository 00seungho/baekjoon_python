a = int(input())
count = 2
for i in range(a):
    count = count + (count -1)
print(pow(count,2))    
