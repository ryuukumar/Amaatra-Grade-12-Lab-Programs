f = open("Class Illustrations/append.txt","rb")
r =f.read(5)
print(r)
print(f.tell())
f.seek(5,1)
print(f.tell())
print(f.read(5))
f.seek(5,0)
print(f.tell())
print(f.read(5))
f.seek(-10,2)
print(f.tell())
print(f.read(5))
