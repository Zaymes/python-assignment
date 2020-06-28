# question 11
# counts occurence of each word

def words_freq(sentence):
    sentence = sentence.lower()
    freq = dict()
    words = sentence.split(" ")

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    
    return freq

print(words_freq('apple apple banana cat dog cat'))






# question 12
# takes input and displays in upper and lowercase

def upper_lower():
    text = str(input('Enter text'))
    print(text.upper())
    print(text.lower())


upper_lower()



# question 13
# prints unique words in sorted form

def csv_sort(sequence):
    words = [word for word in sequence.split(',')]
    print(','.join(sorted(list(set(words)))))

csv_sort('cat, dog, cat, kathmandu, computer, zoo, human')



# question 14
# creates html strings with tags

def html_creator(tag,content):
    element = '<'+tag+'>'+ content+'<'+tag+'/>'
    return element

print(html_creator('a','this is link'))




# question 15
# inserts string in middle of string

def insert_in_middle(str1,str2):
    mid = int(len(str1)/2)
    return str1[:mid]+str2+str1[mid:]

print(insert_in_middle('[[]]', 'Python'))
print(insert_in_middle('{{}}', 'PHP'))
print(insert_in_middle('<<>>', 'HTML'))


# question 16
# sums all items in list

sum_list = lambda x: sum(x)
print(sum_list([1,2,3,4]))


# question 17
# multiplies all items in list

def mul(list):
    result = 1
    for i in list:
        result *= i
    return result


print(mul([1,2,3]))




# question 18
# gets largest number from list

largest = lambda x : max(x)

print(largest([123,456,34,67,1234]))



# question 19
# gets smallest number from list

smallest = lambda x : min(x)
print(smallest([12,13,14]))


# question 20

list_string = ['abc', 'xyz', 'aba', '1221']
count_string = list(filter(lambda x: x[0]==x[-1] and len(x)>2,list_string))
print(len(count_string))


