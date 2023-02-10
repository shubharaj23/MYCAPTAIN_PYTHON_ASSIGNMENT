def circle(r):
    print("area of a circle is:",3.14*r**2)
circle(1.1)
print()    


c={'x':'abc.py','y':'abc.java','z':'abc.c'}
for i in c.keys():
    if c[i]=='abc.py':
        print("enter the file name:","python")
print("file is found")        