# question 1
# max of three numbers

def maximum(a,b,c):
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= x:
        latgest = b
    else:
        largest = c
    return largest


print(maximum(10,-3,4))
    

# question2
# sum all numbers in a list

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum


print(sum_list([1,2,3,4,5,6,7,8,9]))


# question3
# multiply all numbers in list

def product(list):
    prod = 1
    for i in list:
        prod *= i
    return prod


print(product([1,2,3,4]))


# question4
# reverse string

def reverse(string):
    string = string[::-1]
    return string


print(reverse('hello world!!')) 


# question5
# factorial

def Factorial(num):
    if num == 0:  # positive num as i/p considered
        return 1
    else:
        return num * Factorial(num-1)


print(Factorial(8))


# question 6
# check if number is in given range

def in_range():
    upper = int(input('Upper limit of range: '))
    lower = int(input('Lower linit of range: '))
    num = int(input('number to be checked: '))
    return num >= lower and num <= upper


in_range()


# question 7
# calculate number of uppercase and lowercase

def up_low_count(s):
    u_count = 0
    l_count = 0
    for char in s:
        if char.isupper():
            u_count += 1
        elif char.islower():
            l_count += 1
    return u_count,l_count



u,l = up_low_count('The quick Brow Fox 1234')
print('uppercase: ',u,'lowercase: ',l)



# question 8
# returns list with unique elements from previous list

def unique_list(li):
    new_list = []
    for i in li:
        if i not in new_list:
            new_list.append(i)
    return new_list

n=unique_list([1,5,2,3,3,3,3,4,5])
print(n)



# question  9
# check if number is prime

def is_prime():
    num = int(input('Enter natural number: '))
    if num >1:
        for i in range(2,num):
            if num%i == 0 :
                return False
        return True
    else:
        return True



print(is_prime())



# questio 10
# prints even number from list

def print_even(li):
    li = [i for i in li if i%2 == 0]
    print(li)

print_even([1, 2, 3, 4, 5, 6, 7, 8, 9])



# question 11
#  lambda

add_15 = lambda x : x + 15
product = lambda x, y : x * y

print(add_15(15))
print(product(10,20))


# question 12

def multiply_with(num):
    a = int(input('Enter number: '))
    return a*num


print(multiply_with(20))

        


  # question 13

tuple_list = [('a',30),('b',20),('c',70),('d',50)]

print(tuple_list)

tuple_list.sort(key = lambda x: x[1])

print(tuple_list)



# question 14
# sort dictionary by age

dict_list = tuple_list = [{'name':'a','age':30}, {'name':'b','age':20}, {'name':'c','age':10}]

dict_list = sorted(dict_list, key = lambda x: x['age'])

print(dict_list)



# question 15

li =['s',1,2,'{}','f','s','e','t',5,7,34,67,3]

li1 = list(filter(lambda x: (type(x)==int),li))

print(li1)


# question 16

square = lambda x: x*x

cube = lambda x: x*x*x

print(square(2))
print(cube(2))




# question 17

starts_with = lambda x, y : x[0] == y

print(starts_with('man','m'))
print(starts_with('phone','o'))


# question 18

is_number = lambda x: x.isdigit()

print(is_number('1234'))
print(is_number('sad3123'))



# question 19

def fibonacci(n):
    sequence = [0, 1]

    any(map(lambda _: sequence.append(sum(sequence[-2:])), range(2, n)))

    return sequence[:n]

print(fibonacci(14))



# question 20

array1 = [2,4,5,6,7,9,0,13,6]
array2 = [1,3,5,7,9,11]

array_intersection = list(filter(lambda x: x in array1, array2))

print(array_intersection)