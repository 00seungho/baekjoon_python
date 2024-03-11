xywh = input().split()
xywh = list(map(int,xywh))
print(min(xywh[0], xywh[1], xywh[2]-xywh[0], xywh[3]-xywh[1]))