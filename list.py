list=["apple","banna","elephant"]
print(list)

list=["apple","banna","elephant"]
print(len(list))

list=["nn",20,20.6,"2d"]
print(list)

mylist=(("nithin","charan"))
print(mylist)

list=["nn",20,20.6,"2d"]
print(list[2])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[3:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#change list item
list=["hello","world"]
list[0]="hi"
print(list)

list=["hello","world","python"]
list[1:4]=["hi","how"]
print(list)

list=["hello","world","python"]
list.insert(2,"hi")
print(list)

#adding list
list=["nnn","mmm","kk"]
list.append("rrr")
print(list)

x=["nithin","pavan","charan","anil"]
y=["cheetan","mohan"]
x.extend(y)
print(x)

#remove list
x=["nithin","pavan","charan","anil"]
x.remove("anil")
print(x)

x=["nithin","pavan","charan","anil"]
x.pop(2)
print(x)

x=["nithin","pavan","charan","anil"]
x.pop()
print(x)

x=["nithin","pavan","charan","anil"]
del x[0]
print(x)

x=["nithin","pavan","charan","anil"]
x.clear()
print(x)

#loop list
x=["nithin","pavan","charan","anil"]
for x in x:
    print(x)

u=["nithin","pavan","charan","anil"]
for i in range(len(u)):
    print(u[i])

    x=["4r","pavan","charan","67"]
    i=0
    while i<len(x):
        print(x[i])
        i=i+1

#list compreshension
y=["bvhbv","cnvem"," ncsk","jcen"]
n=[x for x in y if "s" in x]
print(n)

y=[x for x in range(10)]
print(y)

y=[x for x in range(20)if x<19]
print(y)


y=["bvhbv","cnvem"," ncsk","jcen"]
n=[x.upper() for x in y ]
print(n)

#sort list
y=["bvhbv","cnvem"," ncsk","jcen"]
y.sort()
print(y)

x=[23,43,1,20,3]
x.sort(reverse=False)
print(x)

y=["bvhbv","cnvem"," ncsk","jcen"]
y.reverse()
print(y)

y=["python"]
y.__reversed__()
print(y)

#join list
x=["nithin"]
y=[2,4,5,]
c=x+y
print(c)

y=["appl","ball","cat"]
m=[2,3,4.2,4]
for x in m:
    y.append(x)
print(y)

y=["appl","ball","cat"]
m=[2,3,4.2,4]
y.extend(m)
print(y)
