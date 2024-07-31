set={"nn","mm","cc"}
print(set)
print(type(set))

set={"apple","banana","cat","apple","cat"}
print(set)

set={"apple","banana",3,True,3.2,"2d"}
print(set)

set={"apple","banana",3,False,3.2,"2d"}
print(set)

set={"apple","banana",3,True,3.2,"2d"}
print(len(set))

set={"apple","banana",3,True,3.2,"2d"}
for x in set:
    print(x)

set={"apple","banana",3,True,3.2,"2d"}
print("graple" in set)

#add set items
set={"apple","banana",3,True,3.2,"2d"}
set.add("grapes")
print(set)

set={"apple","banana",3,True,3.2,"2d"}
nithin={"naik","chouhan"}
set.update(nithin)
print(set)

#remove set items
ithin={"naik","chouhan"}
ithin.remove("chouhan")
print(ithin)

ithin={"naik","chouhan"}
del ithin
print()


#join set
a={"apple","banna"}
b={1,4,2,4}
c=a|b
print(c)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
set=set1.union(set2,set3,set4)
print(set)

a={"aa","bb",2,4}
b={"bb",4,9,4,5}
c=a.intersection(b)
print(c)