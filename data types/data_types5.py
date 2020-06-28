# question 41 
# convert tuple to string

def tuple_to_string(tup):
    if type(tup) not str:
        tup = str(tup)
    str = ''.join(tup)
    return str


tuple1 = ('p','y','t','h','o','n')
string = tuple_to_string(tuple1)
print(string)

print(tuple_to_string(1,2,3,4))





# question 42
# convert list to a tuple

def list_to_tuple(list):
    return tuple(list)


li = [1,2,3,4,5,6,7,8,9]
new_tuple = list_to_tuple(li)
print(new_tuple)


# question 43
# remove an item from tuple

def rmv_tuple_item(tup,item):
    tup = list(tup)
    tup.remove(item)
    tup = tuple(tup)
    return tup

tup = (1,2,3,4,5,6,7,8,9)
tup = rmv_tuple_item(tup,2)
print(tup)




# question 44
# slices a tuple

tup = (1,2,3,4,5,6)

tup = tup[2:4]
print(tup)




# question 45
# find index of item in a tuple

a = (1,1,2,3,4,5,6,7,4)

print('the index of 2 is',a.index(2))
print('the index of 1 is',a.index(1))



# question 46
# length of tuple

 tup = (1,2,3,4,5,6)
 print('length of tuple tup is ',len(tup))