my_dict={
    "name":"yashna",
    "age": 18,
    "grade": "A"
}
# print(my_dict)

# accessing values my key
'''name = my_dict["name"]
age = my_dict["age"]
print(name,age)'''

# modifying dicionary values
# modifying a value
'''my_dict["age"] = 15
my_dict["city"] = "new york"
print(my_dict)

for key,value in my_dict.items():
    print(f"{key}:{value}") 

for key in my_dict.keys():
    print(f"{key}")

for value in my_dict.values():
    print(f"{value}")'''


'''squares={num: num**2 for num in range(1,6)}
print(squares)'''

del my_dict["age"]
print(my_dict)



x=my_dict.get("name")
print(x)

# add
dict = {0:10,1:20}
dict[2]=30
print(dict)

dic1 = {1:10,2:20}
dic2= {3:30,4:40}
dic3 = {5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

