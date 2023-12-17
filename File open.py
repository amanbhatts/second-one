f = open("F:\\python test.txt","rt")
# print(f.read(17))
#print(f.readline())
#print(f.readline())

for x in f:
    print(x)
f.close()

# writing to the existing file
# a , w

# f.write("New learning is added to the training")
# f.close()

# f = open()

f.write("New learning is added to the training")
f.close()

f = open("F:\\python test.txt","rt")
print(f.read())

f = open("F:\\python test.txt","w")
import os