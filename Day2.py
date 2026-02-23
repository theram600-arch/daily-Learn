# # Tuple     A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, ().


# fruits = ('banana', 'orange', 'mango', 'lemon')
# first_fruit = fruits[0]
# second_fruit = fruits[1]
# last_index =len(fruits) - 1
# last_fruit = fruits[last_index]
# print(last_fruit)

# Syntax
# tpl = ('item1', 'item2', 'item3','item4')
# all_items = tpl[0:4]         # all items
# all_items = tpl[0:]         # all items
# middle_two_items = tpl[1:3]  # does not include item at index 3
# print(middle_two_items)



# joining
# tpl1 = ('item1', 'item2', 'item3')
# tpl2 = ('item4', 'item5','item6')
# tpl3 = tpl1 + tpl2
# print(tpl3)




# sets           To create an empty set, we use the set() function. Empty curly brackets {} will create a dictionary.
# adding syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# st.add('item5')
# print(st)

# removing
# syntax
# st = {'item1', 'item2', 'item3', 'item4'}
# st.remove('item2')
# print(st)
# pop
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.pop()  # removes a random item from the set

# # clear
# st = {'item1', 'item2', 'item3', 'item4'}
# st.clear()

# # join
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item5', 'item6', 'item7', 'item8'}
# st3 = st1.union(st2) #st3 = st1 | st2





# dictionary                  A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
# syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print(len(dct))                                                                    



person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

# # print(person['address'])
# # person['skills'].append("html")
# # print(person)
# person['first_name']="hayes"
# person["njdjn"]="dewdeded"
# print(person)

# person.pop("address")
# print(person)









