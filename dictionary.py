# dictionary is data structure that holds in key value pair
# is it similar to js map or object
# more specific it is similar to map 
# keys of a dictionary can be any thing that is hashable
# a hashable means that value which never changes (immutable)
#  string number tuple boolean etc are hashable
#  lists dictionaries are not hashable because its value can change so it can not be a key type
# key value can be input of a hash function that outputs a hash
# dicitonaries has functions: pop(), get(), clear(), items(), values(), keys()


# dictionary

dict = {"name": "samiul"}

# list of dictionary

list = [
    {"name": "samiul"},
    {"name": "samiul"},
    {"name": "samiul"}
]

# iterate through every key
for keys in dict:
    print(dict)

# iterate through every key value
for value in dict.values():
    print(value)

# iterate through every key value
for key , value in dict.items():
    print(key, value)    

# Dictionary comprehension
numbers = [1, 2, 2, 3, 3, 3, 4]
dict2 = { number: number* number for number in numbers} 
print(dict2)

frq = {}

for number in numbers:
    frq[number] = frq.get(number, 0) + 1


print(frq)