N = int(input())
gomgom = 0
dic = {}
for i in range(N):
    msg = input()
    if msg == "ENTER":
        dic ={}
        continue
        
    if msg in dic:
        continue
    else:
        gomgom +=1
        dic[msg] = ""

print(gomgom)