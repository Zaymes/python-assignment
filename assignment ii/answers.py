# question 1
# create variable and assign paragraph to it

paragraph = '"Python is a great language!", said Fred. "I don\'t ever remember having this much fun before."'

print(paragraph)




# question 2
# program to check if it is a leap year

year = 2000

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("{} is a leap year".format(year)
            else:
                print("{} is not a leap year".format(year))
        else:
            print("{} is a leap year".format(year))
    else:
        print("{} is not a leap year".format(year))

is_leap_year(2000)
is_leap_year(2004)
is_leap_year(1998)









# question 3
# print anagrams from paragraph



import collections

paragraph ="this this is the question i i i am doing"
paragraph = paragraph.lower()
paragraph = paragraph.split(' ')
new = []

# make the list containing sorted strings that acts as map to 
# original paragraph list containing words in sequence

for word in paragraph:
    new.append(''.join(sorted(word)))

# count occurence of words that have same sorted value

occurrences = collections.Counter(new)


# make dictionary that stores the anagrams in list as values
anagrams = {}
for i,items in enumerate(new):
    if occurrences[items] >=2:

        if items not in anagrams.keys():
            anagrams[items] =[paragraph[i]]

        else:
            anagrams[items].append(paragraph[i])

  
print('The anagrams present in paragraph are: ')
for words in anagrams.values():
    print(words)






# question 4
# create list, apend and check id, sort

names = []
print('id of list is {}'.format(id(names)))

names.append('James')
names.append('Krishna')
print('id after appending of list is {}'.format(id(names)))

names.append('Saileh')
names.append('Rajad')
print('id after appending of list is {}'.format(id(names)))

names.append('Dhadkan')
print('id after appending of list is {}'.format(id(names)))
# id is unchanged

names.sort()
print(names)





# question 5
# list of tuple with first name, last name and age
# sort with different key parameters

people =[]

people.append(('James','Shrestha',21))
people.append(('Krishna','Rauniyar',37))
people.append(('Dhadkan','Shrestha',19))
people.append(('Rajad','Shakya',22))
people.append(('Aakrish','Maharjan',22))

# sorting the list on age key of tuple
people = sorted(people, key = lambda x: x[2])
print(people)






# question 6
# loop on list of names to find 'john'

names = ['Ram','Hari', 'Shyam', 'John', 'Harry', 'Thomas', 'Jonas', 'James']

search_result = 'Not Found'
for i, name in enumerate(names):
    if name == 'John':
        search_result = '{} found in index {}'.format(name,i)
        break
print(search_result)






# question 7
# print the names from list of tuple for value, young or old from calculated average

from statistics import mean

people =[]

people.append(('James','Shrestha',21))
people.append(('Krishna','Rauniyar',None))
people.append(('Dhadkan','Shrestha',19))
people.append(('Rajad','Shakya',22))
people.append(('Aakrish','Maharjan',None))

valid_ages = [ele[2] for ele in people if ele[2] is not None]
mean_age = mean(valid_ages)

for person in people:
    try:
        if person[2] >= mean_age:
            print('{} {} is older'.format(person[0],person[1]))
        else:
            print('{} {} is younger'.format(person[0],person[1])) 
    except TypeError:
        print('{} {} age unknown'.format(person[0],person[1]))






# question 8
# checks if number is prime or not

def is_prime():

    num = int(input('Enter the number: '))

    if num > 1:

        for i in range(2,num,2):
            if num%i == 0:
                return False
        return True
    
    else:
        print('Not valid number')



is_prime()







# question 9
# binary search function

def binary_search(li,item):

    length = len(li)
    half = int(length/2)
    item_index = half # to preserve index
    result = -1

    while length != 1: # loop until last element left on list

        # slice list to half according to comparison on the middle item
        if item > li[half]:
            li = li[half:]
            length = len(li)
            item_index = item_index + int(length/2)

        else:
            li = li[:half]
            length = len(li)
            item_index = item_index - int(length/2)

        half = int(length/2)
        if item == li[half]:
            result = item_index
            return result

    return result




result = binary_search([1,2,4,5,7,9,13,14,34],0)
if result == -1:
    print('Item not found')
else:
    print('The index of required item is {}'.format(result))






# question 10
# function to convert camel-cased to snake and kebab cased

from functools import reduce

def change_from_camel(camel_str):

    snake_str = reduce(lambda x,y: x + ('_' if y.isupper() else '')+y,camel_str).lower()
    kebab_str = snake_str.replace('_','-')

    return snake_str, kebab_str


snake_str, kebab_str = change_from_camel('theCamelCasedWordIsHere') 

print(snake_str)
print(kebab_str)      






# question 11
# filename and extension

filename = 'README.txt'

# extension of filename assuming 3 letter extension
print('The extension of {}  is {}'.format(filename,filename[-3:]))

# name of file without extension
print('The filename of {} without extension is {}'.format(filename,filename[:-4]))

    





# question 12
# checks if the given word is pilandrome

def is_pilandrome(word):
    return word == word[::-1]

print(is_pilandrome('tattarrattat'))
print(is_pilandrome('bob'))
print(is_pilandrome('bobby'))






# question 13
# function that creates csv file

import csv

def create_csv(filename,tuple_list):

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(('name', 'adress', 'age'))
        writer.writerows(tuple_list)


create_csv('names.csv',[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)])





# question 14
# function to read csv 
# and returns list of dicts

import csv

def csv_to_dict(filename):

    dict_list = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            temp_dict = {}
            temp_dict[header[0]] = row[0]
            temp_dict[header[1]] = row[1]
            temp_dict[header[2]] = row[2]
            dict_list.append(temp_dict)

    return dict_list

names = csv_to_dict('names.csv')






# question 15
# banking customer class


class Customer:

    def __init__(self, acc_name, acc_number, phone_number, adress,e_mail, acc_balance):
        self.acc_name = acc_name
        self.acc_number = acc_number
        self.phone_num = phone_number
        self.adress = adress
        self.e_mail = e_mail
        self.acc_balance = acc_balance

    def get_balance(self):
        return self.acc_balance
    
    def display_info(self):
        print('name: {}\naccount number: {}\nphone number: {} \nadress {} \ne-mail: {}'.format(self.acc_name, self.acc_number, self.phone_num, self.adress, self.e_mail))

    def check_balance(self):
        print(self.get_balance())


    def do_payment(self, amount):
        self.acc_balance = self.acc_balance - amount







# question 16
# ludo game

class Player:

    def __init__(self, color):
        self.color = color
        self.to_dest = 0
        self.inside_home = 4
        self.position = 0

    def get_outside(self):
        print('Gets outside from home to begin play on 1 or 6 from dice')

    def move_forward(self):
        print('Moves forward')

    def get_to_dest(self):
        print('gets to destination')
    
    def reach_dest(self):
        self.inside_home -= 1
        self.to_dest += 1

        if self.to_dest == 4:
            self.position = 1
    



# question 17
# program to act as calculator for 2 numbers

import operator

operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def calculator():

    while True:
    
        try:
            num1 = float(input('num1: '))
            num2 = float(input('num2: '))
        except ValueError:
            print('enter the numeric value')
            continue


        operator = input('Enter operator')

        op = operatorlookup.get(operator)

        if op is not None:
            try:
                result = op(num1,num2)
                print(result)
            except ZeroDivisionError:
                print('Cannot divide by zero')
        else:
            result = "unknown operator"
        

calculator()

    
    


# question 18
# json

import json


# serialize
info = {'name':'James', 'age':16}

with open('info.json','w') as f:

    json.dump(info, f, indent=2 )
    f.close()


# deserialize
with open('info.json') as f:
    data = json.load(f)
    print(data)





# question 19
# paranthesis validity

def is_valid(par_str):
    opening = ['[','{','(']
    closing = [']','}',')']
    result = []

    for i in par_str:
        if i in opening:
            result.append(i)
        elif i in closing:
            if closing.index(i) == opening.index(result[-1]):
                result.pop()
            else:
                break
    
    if len(result) == 0:
        return True
    else:
        return False        

is_valid('[{()}()]')

is_valid('{{{')



# question 20
# three elements that sums to zero


from itertools import combinations
   
comb = combinations([-25, -10, -7, -3, 2, 4, 8, 10],3) 
  
for i in list(comb):
    if sum(i) == 0:
        print('Three numbers having sum 0 {}'.format(i))





