# question 31
# iterate over dictionary using for loop

dict1 = {0: 10, 1: 20, 2: 10, 3: 20, 4: 10, 5: 20}
for key in dict1.keys():
    print(key,dict1[key])



# question 32
# generate and print dictionary

def generate_dict(n):
    dict1 = {}
    for i in range(1,n+1):
        dict1[i] = i*1
    print(dict1)


generate_dict(5)



# question 33
# dictionary with keys from 1-15

dict_15 = {}
for i in range(1,16):
    dict_15[i] = i*i
print(dict_15)




# question 34
# merge two dictionaries


def merge(dict1,dict2):
    return dict1.update(dict2) #merge dict2 to dict1


dict1 = {'a': 10, 'b': 8} 
dict2 = {'d': 6, 'c': 4} 

merge(dict1,dict2)
print(dict1)



#question 35
#same as 31



# question 36
# sum all items in dictionary

def dict_sum(dict1):

    sum =0
    for item in dict1.values():
        sum += item
    
    return sum

print('sum is ',dict_sum({'a':1,'b':2,'c':3}))






# question 37
# multiply all items i dictionary


def dict_mul(dict1):

    product = 1

    for item in dict1.values():
        product *= item
    return product


print('Product is',dict_mul({'a':1,'b':2,'c':3}))



# question 38
# removes key from dictionary

d ={'a':1,'b':2,'c':3}

def remove_key(d, key):
    try:
        del d[key]
    except KeyError:
        print("key",key,"is not found")

remove_key(d,'b')
print(d)



# question 39
# unpack tuple to variables

student = ('James Shrestha', 21, 'BEX', 'Kathmandu')
(name, age, faculty, adress) = student

print('name: ', name)
print('age: ', age)
print('faculty: ', faculty)
print('adress: ', adress)


# question 40
# add an item to tuple

def add_item(tuple1, item):
    tuple1 += (item,)
    return tuple1

tup = (1,2,3,4)
print(add_item(tup,5))

