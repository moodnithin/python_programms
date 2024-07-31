for x in "nithin":
    print(x)

#break statement
n={"apple","banana","ball"}
for x in n:
    if x=="ball":
        break
    print(x)


n=["apple","banana","ball"]
for x in n:
    if x=="ball":
        continue
    print(x)
#range
for x in range(5):
    print(x)

for x in range(2,5):
    print(x)

#nested loop

a=["nithin","pavan","anil"]
b=["hero","heerion","actor"]

for x in a:
    for y in b:
        print(x,y)