# set datatype

"""
What is set
How to define a set
set is unordered and unchangeable
Accessing set item
updating set
looping over set
Joining set
removing of items
set method
"""

set_list_1 = {1,2,3,4,5,6,7,8}
set_list = set((10,2,3,4,5,6,5,7,8,1))
# print(set_list)
# print(set_list[2])
# print(len(set_list))

# for i in set_list:
#   print(i)

# print(2 not in set_list)

# set_list_1.update(set_list)
# set_list_1.add("mango")
# set_list_1.remove("mango")
set_item_3 = {'apple','grape','orange'}
set_item_4 = {'pen','book','brain'}
new_item = set_list_1.union(set_item_3, set_item_4)
# print(new_item)

# Set methods
set_list_1.discard(2)
# print(set_list_1)

# mathematical methods of set

# set_list_1.difference(set_list_2)
# set_list_1.add(set_list_2)
# print(set_list_1.difference(set_list_2))
# print(set_list_1.intersection(set_list_2))

