this_dict = {
    "brand" : "ford",
    "model" : "mustang GT",
    "year" : "1990"
}
print(this_dict)
this_dict.update({'brand' : 'ford', 'brand':'nissan'})
print(this_dict)
print(this_dict.get("brand"))

# change the values
this_dict.pop("brand")
print(this_dict)

# for loop
for x in this_dict:
    print(this_dict[x])

# copying - copy , dict()

this_dict = {
    "brand": "ford",
    "model": "mustang GT",
    "year": "1990"
}
my_dict = this_dict.copy()
print(my_dict)

