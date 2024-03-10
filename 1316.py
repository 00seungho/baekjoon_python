def split_into_groups(word):
    groups = []  
    current_group = word[0] 
    for char in word[1:]:
        if char == current_group[-1]:
            current_group += char
        else:
            groups.append(current_group) 
            current_group = char  
    groups.append(current_group)
    return groups

def is_group(gropus):
    for i in range(len(gropus) - 1):
        for j in range(i+1,len(gropus)):
            if gropus[i][0] == gropus[j][0]:
                return False
    return True
N = int(input())
count = 0
for i in range(N):
    words = input()
    split_words=split_into_groups(words)
    if is_group(split_words):
        count +=1
print(count)
            