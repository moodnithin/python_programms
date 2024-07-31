def my_function():
    print("hello nithin")
my_function()

def my_function(nithin):
    print(nithin)
my_function("name")
my_function("age")
my_function("2d")
my_function(22)
#number argument

def my_function(fname,lname):
    print(fname+lname)

my_function("mood","nithin")



def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


def my_function(*n):
    print(n[3])
my_function("nnv","fjen","kmecve","jfwnif","njj")

def my_function(child,child2,child3,child4):
    print(child+" "+child2)
my_function(child2="nithin",child="pavan",child3="anil",child4="chentan")

def my_function(**child):
    print(child["last"])
my_function(fname="nithin",middle="pavan",last="anil",sure="chentan")

#dafult function

def my_function(state="telagana"):
    print("i m from"+" "+state)
my_function("bengalur")
my_function("mp")
my_function()
my_function("odisa")

#pass list

def my_function(age):
    for x in age:
        print(x)
ages=[22,234,43,34]
my_function(ages)

#return statement

def my_function(x):
    return 9*x
print(my_function(0))
print(my_function(3))

#combinational keywords

def my_function(c,w,e,d,q):
    print(c*w*e+d-q)
my_function(2,6,8,3,5)

