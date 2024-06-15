"""Python dictionary is like hash tables in any other language with the time complexity of O(1)"""

"""Counters
A counter is a sub-class of the dictionary. It is used to keep the count of the elements in an iterable
in the form of an unordered dictionary where the key represents the element in the iterable and value
represents the count of that element in the iterable. This is equivalent to a bag or multiset of other
languages.

Example: Python Counter Operations

from collections import Counter
   
# With sequence of items 
print(Counter(['B','B','A','B','C','A','B','B','A','C']))
   
# with dictionary
count = Counter({'A':3, 'B':5, 'C':2})
print(count)
 
count.update(['A', 1])


Counter({'B': 5, 'A': 3, 'C': 2})
Counter({'B': 5, 'A': 3, 'C': 2})
Counter({'B': 5, 'A': 4, 'C': 2, 1: 1})
print(count)"""


"""
ChainMap
A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries. When a key is needed to be found then all the dictionaries are searched one by one until the key is found.

Example: Python ChainMap Operations

from collections import ChainMap
     
     
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
     
# Defining the chainmap
c = ChainMap(d1, d2, d3)
print(c)
 
print(c['a'])
print(c['g'])
Output

ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
1
"""


"""
NamedTuple
A NamedTuple returns a tuple object with names for each position which the ordinary tuples lack. For example, consider a tuple names student where the first element represents fname, second represents lname and the third element represents the DOB. Suppose for calling fname instead of remembering the index position you can actually call the element by using the fname argument, then it will be really easy for accessing tuples element. This functionality is provided by the NamedTuple.

Example: Python NamedTuple Operations

from collections import namedtuple
     
# Declaring namedtuple()
Student = namedtuple('Student',['name','age','DOB'])
     
# Adding values
S = Student('Nandini','19','2541997')
     
# Access using index
print ("The Student age using index is : ",end ="")
print (S[1])
     
# Access using name
print ("The Student name using keyname is : ",end ="")
print (S.name)
Output
The Student age using index is : 19
The Student name using keyname is : Nandini
"""
