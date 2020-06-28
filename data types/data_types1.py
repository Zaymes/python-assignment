# from auestions 1 to 10


# question1
# counts number of characters

def count(str):
    freq = {}
    for i in str:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print(freq)
    

count('missipi')




# question 2
# prints string first and last 2 chars combined

def first_last_str(str):
    if len(str) < 2:
        return ''
    else:
        return str[:2]+str[-2:]
        

print(first_last_str('python'))




# question 3
# replace by $

def change_chars(str):
    result = str[0]
    for i in str[1:]:
        if i in str[0]:
            result = result+'#'
        else:
            result += i
    print(result)


change_chars('jojo')




# question 4
# two strs combined seperated by a whitespace

def combine(str1, str2):
    return str2[:2]+str1[2]+' '+str1[:2]+str2[2]


print(combine('abc', 'def'))




# question 5
# add ing or ly to the end

def to_ing(str):
    if len(str) > 2:
        if 'ing' in str[-3:]:
            return str+'ly'
        else:
            return str+'ing'
    else:
        return str


print(to_ing('abc'))
print(to_ing('abcing'))
print(to_ing('aasbdjh'))



# question6
# replace not poor by poor

def not_poor(str1):

    snot = str1.find('not')
    spoor = str1.find('poor')
    if spoor > snot and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:(spoor+4)], 'good')
        return str1
    else:
        return str1



print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))





# question 7
# returns longest string

def longest(words):
    return max(words, key=len)


print(longest(['a','ab','abcd','abc','de','def']))



# question 8
# removes nth char from non-empty string

def remove(str, n):
    return str[:n]+str[n+1:]


print(remove('abcdef', 2))




# question 9
# exchange first and last chars of string

def exchange(str):
    return str[-1]+str[1:-1]+str[0]

print(exchange('abcdef'))




# question 10
# remove characters od odd index

def remove_odd_seq(str):
    return str[0::2]


print(remove_odd_seq('abcdefg'))