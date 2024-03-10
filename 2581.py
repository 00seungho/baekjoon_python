def isPri(number):
    if number == 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

M = int(input())
N = int(input())

Pri = []
for i in range(M,N+1,1):
    if isPri(i):
        Pri.append(i)
    else:
        continue
if len(Pri) == 0:
    print("-1")
else:
    print(sum(Pri))
    print(Pri[0])