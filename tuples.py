mytuple=("aa","bb","cc")
print (mytuple)

#duplicate values
mytuple=("aa","bb","cc","bb","aa")
print (mytuple)
#tuple len

mytuple=("aa","bb","cc","bb","aa")
print (len(mytuple))

m=("nithin",)
print(type(m))

m=("nithin")
print(type(m))

a=("apple","bnns","cat")
b=(2,4,5,3)
c=(True,False,True)
print(a)
print(b)
print(c)


tuple=("apple",22,44.5,"2d")
print(type(tuple))
print(tuple)

#access tuple
a=("apple","bnns","cat")
print(a[0:1])

a=("apple","bnns","cat")
if "apple" in a:
    print("no, 'apple' is in a")


#update in tuple
x = ("apple", "banana", "cherry")
y = list(x)
y.append("apple")
print(y)


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry")
for x in fruits:
    print(x)


fruits = ("apple", "banana", "cherry")
for i in range(len(fruits)):
    print(fruits[i])