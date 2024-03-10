def isPri(number):
    if number == 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

a = int(input())
N = input().split()
N = list(map(int,N))
count= 0
for i in range(a):
    if isPri(N[i]):
        count+=1
    else:
        continue

print(count)