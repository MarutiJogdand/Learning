'''MAP function
Input : function,list
output : iterable object

Defination : Map function is used to process on each and every element of list.

Syntax : map(function , list)
'''

# Basic Operation

lists = [1,2,3,4,5]
squares = list(map(lambda x: x**2, lists))
print('square list :', squares)


