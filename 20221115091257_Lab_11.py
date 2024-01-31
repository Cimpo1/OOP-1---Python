#1. 3 {'red': 10, 'blue': 20, 'green': 30}
#2. 5 {'red': 10, 'blue': 20, 'green': 30, 'yellow': 40, 'orange': 50}
"""
3.

red
blue
green
yellow
orange
"""
'''
4.

red 10
blue 20
green 30
yellow 40
orange 50
'''
#5. 50 yellow
"""
6.

>>> sum(colours.values())
150
"""
"""
7.

>>> for x in colours:
    colours[x] += 1
"""
'''
8.

>>> for x in sorted(colours):
    print(x)
    
blue
green
orange
red
yellow
'''
'''
9.

>>> for x in sorted(colours.items()):
    print(x)
    
('blue', 21)
('green', 31)
('orange', 51)
('red', 11)
('yellow', 41)
'''
'''
10.

>>> print(colours['pink'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'pink'
'''
'''
11.

>>> print(colours.get('red'))
11
>>>  print(colours.get('pink'))
None
'''
'''
12.

>>>  print(colours.get('red', 1099), colours.get('pink', 1099))
11 1099
'''
'''
13.


>>> x = dict()
>>> y = x
>>> z = x.copy()
>>> print(x is y, x is z)
True False
>>> print(x == y, x == z)
True True
>>>  z[2.0] = 'two'
>>> y[3.14159] = 'pi'
>>> y[2.71828] = 'e'
>>> print(x, z)
{3.14159: 'pi', 2.71828: 'e'} {2.0: 'two'}
>>> y.clear()
>>> print(x, z)
{} {2.0: 'two'}

x is y so x dissapears
'''
'''
14.


>>> x = {'a': 10, 'c': 11, 'z': 12 }
>>> y = {'z': 12, 'a': 10, 'c': 11 }
>>> print(x == y)
True
>>> y['z'] -= 1
>>> print(x == y)
False


'''
'''
15.


>>> from string import ascii_lowercase
>>> letters = dict.fromkeys(ascii_lowercase, 0)
>>>  print(letters)
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
>>> colours = ('red', 'green', 'blue', 'black', 'magenta')
>>> cdict = dict.fromkeys(colours, 0.0)
>>> print(cdict)
{'red': 0.0, 'green': 0.0, 'blue': 0.0, 'black': 0.0, 'magenta': 0.0}


'''
'''
16.


>>> keys = [2001, 2006, 2011, 2016, 2021]
>>> values = [1039534, 1620693, 1649519, 1704694, 1762949]
>>> pop = dict(zip(keys, values))
>>> print(pop)
{2001: 1039534, 2006: 1620693, 2011: 1649519, 2016: 1704694, 2021: 1762949}


'''
'''
17.


>>> print(2001 in pop, 2002 in pop)
True False
>>> print(1649519 in pop)
False
>>> print(1649519 in pop.values()) 
True


'''
'''
18.



>>> inpop = dict(zip(pop.values(), pop.keys()))
>>> inpop
{1039534: 2001, 1620693: 2006, 1649519: 2011, 1704694: 2016, 1762949: 2021}


'''
d = {}
file = open('alice.txt')
text = file.read()
Y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' ,'z']
file.close()
for i in Y:
    u = text.count(i)
    d[i]= u
print(d.items())
print('\n', len(Y))

def clean(word):
    '''Strip away leading or trailing punctuation and convert to lower case.'''
    return word.strip('?!@#$%^&*();:.[],\'\"-').lower()
x = text.split(' ')
y = []
for i in x:
    u = i.split('--')
    for r in u:
        h = r.split('\n')
        for t in h:
            O = clean(t)
            y.append(O)
fg = {}
for i in y:
    if fg.get(i) == None:
        fg[i] = 1
    else:
        fg[i] += 1

del fg['']

def get_second(x):
    '''Returns the second element of sequence 'x'.'''
    return x[1]

descending_items = sorted(fg.items(), key = get_second,  reverse=True)
print('\n')
for x in range(10):
    print(descending_items[x])
    
file2 = open('glass.txt')
text2 = file2.read()
file2.close()
x = text2.split(' ')
P = []
for i in x:
    u = i.split('--')
    for r in u:
        h = r.split('\n')
        for t in h:
            O = clean(t)
            P.append(O)
ff = set()
for i in P:
    if i not in ff:
        ff.add(i)
ff.discard('')

print('\n', len(ff))

ju = []
for u in fg:
    ju.append(u)

for i in ff:
    if i not in ju:
        ju.append(i)
print('\n', ju)



jh = []
for i in ff:
    if i in y:
        jh.append(i)

print('\n', jh)

ji = []
for i in y:
    if i not in ff:
        ji.append(i)

fi = {}
for yu in ji:
    if fi.get(yu) == None:
        fi[yu] = 1
    else:
        fi[yu] += 1

del fi['']

ds = sorted(fi.items(), key = get_second,  reverse=True)

print('\n', ds[0])