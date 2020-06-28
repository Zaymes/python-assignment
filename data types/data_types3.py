# question 21
# sorts in increasing order by the last element in tuple

def sort_tuple_list(tuples):

    tuples.sort(key = lambda x: x[1])
    return tuples


print(sort_tuple_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))




# question 22
# remove duplicates from list

sample_list = [1,2,1,24,5,4,6,7,4,2,5,7,4,3,6,7]

print('Original list', sample_list)
unique_list=[]

[unique_list.append(i) for i in sample_list if i not in unique_list]

print(unique_list)




# question 23
# checks if list is empty

def list_is_empty(list):
    return len(list)==0

a=[1,2]
b=[]

print(list_is_empty(a))
print(list_is_empty(b))



# question 24
# clone list

def clone_list(li1):
    list_copy = li1[:]
    return list_copy


odd = [1,3,5,7,9]
print(clone_list(odd))




# question 25
# checks if all dictionaries in list are empty or not

def empty_dict(dict_list):
    for item in dict_list:
        if bool(item):
            return False
    return True


print(empty_dict([{},{},{}]))
print(empty_dict([{1,2},{},{}]))



# question 26
# insert string to begining of all items in list


def add_to_begining(lst,str):

    str += '%s'
    lst = [str % i for i in lst]
    return lst


print(add_to_begining([1,2,3,4],'emp'))



# question 27
# replace last element of a list with new list


def replace_last_ele(lst1,lst2):
    return lst1[:-1]+lst2

print(replace_last_ele([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))


# question 28
# add key to dictionary

def add_to_dict(dict,key,value):
    dict[key] = value
    return dict

d = {0: 10, 1: 20}

print(add_to_dict(d,2,30))





# question 29
# concatenate dictionaries to create new

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic4 = {**dic1,**dic2,**dic3}


print(dic4)





# question 30
# checks if given key is already present in a dictionary

def key_exists(dic,key):
    if key in dic.keys():
        return True
    return False

print(key_exists({1:10, 2:20},1))
print(key_exists({1:10, 2:20},0)) 






