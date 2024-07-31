n=("apple","ball","cat")
m=iter(n)
print(next(m))
print(next(m))
print(next(m))

o="apple"
print(o)


x="nithin"
m=iter(x)
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))


class Myfunctions:
    def __iter__(self):
        self.n=1
        return self
    
def __next__(self):
    x=self.n
    self.a+=2-1
    return x
myclass=Myfunctions()
myiter=iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNumbers:
  def __iter__(self):
    self.a = 3
    return self

  def __next__(self):
    x = self.a
    self.a += 3
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
