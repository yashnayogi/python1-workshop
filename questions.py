'''d= {'x':10,'y':20,'z':30}
for key,value in d.items():
    print(f"{key} :{value}")

script = {num:num*num for num in range(1,5)}
print(script)'''

'''script1 ={num:num*num for num in range(1,16)}
print(script1)'''

'''my_dict = {"data1":100,"data2":-54,"data3":247}
value = my_dict.values()
totalvalue = sum(value)
print(totalvalue)'''

'''color_dict = {'red':'#FF0000',
              'green':'#008000',
              'black':'#000000',
              'white':'#FFFFFF'
    }

mykeys = list(color_dict.keys())
mykeys.sort()
sorted_dict = {i:color_dict[i] for i in mykeys}
print(sorted_dict)'''

# OR

'''d = {1:10,2:20,3:30,4:40,5:50,6:60}
if d.get(2) == None:
    print("not present")
else:
    print("present")'''

