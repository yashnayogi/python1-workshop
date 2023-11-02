#set is an unordered collection 

#methods and operators

#operating a set
my_set = {1,2,3}

#adding element
my_set.add(4)


#remove element
my_set.remove(2)			
my_set.discard(5)

my_set.add(5)
my_set.add(2)

print(my_set)


#sets operations:
'''union: union()
intersection: intersection()
Difference: difference()
symmetric symmetric_difference()'''


set1 = {1,2,3,4}
set2={4,5,6,7}

set3 = set1.union(set2)
print(set3)

set4 = set1.intersection(set2)
print(set4)
'''intersection = find_intersection(set1,set2)'''

set5 = set1.difference(set2)
print(set5)

set6 = set1.symmetric_difference(set2)
print(set6)

employees = ["corey","jin","steven","april","judy","jenn",""]
gym_members = ["april","john","corey"]
developers = ["judy","corey","steven","jane","april"]
result = set (gym_members).intersection(developers)
print(result)
