MY_dict={"salman":25,"bob":29}
MY_dict
MY_dict={"salman":25,"bob":29}
{'salman': 25, 'bob': 29}

Nested dictionaries

my_dict={"sam":{"age":25,"weight":35},"bo0b":{"age":25,"weight":45}}
my_dict
{'sam': {'age': 25, 'weight': 35}, 'bo0b': {'age': 25, 'weight': 45}}

PRINTING KEY VALUES

for key in my_dict:
    print(key)
sam
bo0b

PRINTING VALUES

for values in my_dict.values():
    print(values)
{'age': 25, 'weight': 35}
{'age': 25, 'weight': 45}

KEY AND VALUE PAIR TOGETHER

for key,value in my_dict.items():
    print('key :'  ,str(key), 'value :',str(value))
key : sam value : {'age': 25, 'weight': 35}
key : bo0b value : {'age': 25, 'weight': 45}
    
PARTICULAR KEY IS PRESENT

2
if 2 in my_dict:
    print("my_dict has key 2")
else :
    print("my_dict doesnt contain key 2")
my_dict doesnt contain key 2

SHALLOW COPY

my_dict={1:['a','b'],2:['c','d']}
my_dict={1:['a','b'],2:['c','d']}
my_dict
my_dict
{1: ['a', 'b'], 2: ['c', 'd']}
my_dict_copy
my_dict_copy=my_dict.copy()
my_dict_copy
{1: ['a', 'b'], 2: ['c', 'd']}
my_dict
my_dict[2][0]="z"
my_dict
{1: ['a', 'b'], 2: ['z', 'd']}
ct_copy
my_dict_copy
{1: ['a', 'b'], 2: ['z', 'd']}

DEEP COPY

my_dict={1:['a','b'],2:['c','d']}
my_dict={1:['a','b'],2:['c','d']}
my_dict
{1: ['a', 'b'], 2: ['c', 'd']}
my_dict_copy
import copy
my_dict_copy=copy.deepcopy(my_dict)
my_dict_copy
{1: ['a', 'b'], 2: ['c', 'd']}
my_dict
my_dict[2][0]='z'
my_dict
{1: ['a', 'b'], 2: ['z', 'd']}
my_dict_copy
my_dict_copy
{1: ['a', 'b'], 2: ['c', 'd']}

Built in function in dictionaries

my_dict
my_dict.clear()
my_dict
{}
my_dict={1:['a','b'],2:['c','d']}
my_dict
my_dict={1:['a','b'],2:['c','d']}
my_dict
{1: ['a', 'b'], 2: ['c', 'd']}
value_of_2=my_dict.get(2)
value_of_2
​
['c', 'd']
my_dict={1:['a','b'],2:['c','d'],3:['e','f']}
my_dict
my_dict={1:['a','b'],2:['c','d'],3:['e','f']}
my_dict
{1: ['a', 'b'], 2: ['c', 'd'], 3: ['e', 'f']}
my_dict.popitem()
(3, ['e', 'f'])
my_dict
my_dict
{1: ['a', 'b'], 2: ['c', 'd']}
my_dict.pop(2)
['c', 'd']
my_dict
my_dict
{1: ['a', 'b']}
adding or updating
my_dict={'a':2,'b':3,'c':4}
_dict
my_dict
{'a': 2, 'b': 3, 'c': 4}
my_dict
my_dict.update({'a':250,'c':100})
my_dict
{'a': 250, 'b': 3, 'c': 100}
