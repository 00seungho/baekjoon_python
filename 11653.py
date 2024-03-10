N = int(input())
flag = 2 
while N != 1:
    if N % flag != 0:
        flag += 1
    else:
        N //= flag
        print(flag)