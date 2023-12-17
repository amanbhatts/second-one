

a = "Hello World"
print(a[5])

a = "Hello World"
print(len(a))

#check String - checks if character or a phrase is present in the string

text = "I live in bangalore"
print("liv" in text)

text = "I live in bangalore"
print("mumbai" not in text)

a = "Hello World*"
print(a[9:11])

#slice from start
#leave the start Index

a = "Hello World*"
print(a[:11])

a = "Hello world*"
print(a[2:])

a =" Hello World"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H","J"))

a = "hello,world,people,men,women"
print(a.split(","))
print(a.split("o"))
b = "combined all these"
c = a+" "+b
print(c)