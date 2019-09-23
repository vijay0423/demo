class Python:
    """sample class to test all python programms in this example"""#documentational string it is a optional statement
    a=1#static variables
    b=2
    c=3
 def __init__(self):#to initialize the non static variables
     print("in constructor of Python")#whenever we create the object on that time constructor method will be executed
     self.x=4
     self.y=5
     self.z=6
 def m1(self):
     print("in m1 of Python")
     p=7
     q=8
     r=9
     print(P)
     print(q)
     print(r)
 def m2(self):
     print("in m2 of Python")
 def modify(self):
     Python.a=Python.a+1
     self.x=self.x+4
 def display(self):
     print(Python.a)
     print(Python.b)
     print(Python.c)
     print(self.x)
     print(self.Y)
     print(self.z)
     self.m1()
     self.m2()
 def __del__(self):
     print("in destructor of Python")#whenever we can delete the object on that time destructor method will be executed
class Jango(Python):
    d=10
 def __init__(self):
     self.w=11
 def m2(self):
     print("in m2 of Jango")
 def m3(self):
     print("in m3 of Jango")
 def display(self):
     print(Jango.d)
     print(self.w)
     self.m2()#sub class
     self.m3()
     print(Jango.a)
     print(Jango.b)
     print(Jango.c)
     print(self.x)
     print(self.y)
     print(self.z)
     self.m1()
r1=Jango()
print(r1)
r1.m1()
r1.m2()
r1.m3()
r1.display()

     
     
     
