def my_len(x):
    rs = 0
    if type(x) != int:
        for f in x: # f is not needed
            rs += 1
    return rs

assert my_len([]) == 0
assert my_len('Marianopolis') == 12
assert my_len((1, 5, 9, 2)) == 4

def my_count(e,r):
    rs = 0
    for g in e:
        if e[(g-1)] == r:
            rs += 1
    return rs

k = [1,2,3,3]
assert my_count(k,1) == 1
assert my_count(k,3) == 2
assert my_count(tuple(k), 4) == 0

def my_find(t,h):
    rs = 0
    for r in range(my_len(t)):
        if t[r] == h:
            return rs
        rs +=1
    return -1
j = ["orange", "red", "yellow", "green"]
assert my_find(j, "blue") == -1
assert my_find(j, "green") == 3
assert my_find(tuple(j), "orange") == 0

def product(y):
    if (type(y) is list) or (type(y) is tuple):
        rs = 1
        for t in y:
            rs *= t
        return rs
    else:
        return print('Invalid')
    
assert product([]) == 1
assert product([3]) == 3
assert product([3, 7, 5]) == 105
assert product((2, -5, 7, 3, 19)) == -3990

def is_cdn_postal_code(st):
    if type(st) != str:
        return print('Invalid')
    if st.isupper() != True:
        return print('Invalid')
    rs = list(st)
    if (rs[0] != 'Z') and rs[1].isnumeric() and rs[4].isnumeric() and rs[6].isnumeric():
        return True
    else:
        return False

assert is_cdn_postal_code("H2Y 1B5")
assert is_cdn_postal_code("S7K 1L9")
assert is_cdn_postal_code("X1A 1E5")
assert is_cdn_postal_code("Y1A 1A4")
assert not is_cdn_postal_code("H4T 16Z")
assert not is_cdn_postal_code("Y1A1A5")
assert not is_cdn_postal_code("Z4A 2N5")

def is_sorted(x):
    if my_len(x) == 0:
        return True
    t = x[0]
    for d in x:
        if (t<=d) != True:
            return False
        t = d
    return True

assert is_sorted([]) # empty list is sorted
assert is_sorted([2]) # list with one element is sorted
assert is_sorted([1, 2])
assert not is_sorted([2, 1])
assert is_sorted((1, 100, 110, 2000, 2000, 123456, 10**10, 10**19))
assert not is_sorted([1, 2, 3, 4, 4, 4, 6, 5])

def my_split(a_str):
    list1 = []
    if a_str == '':
        return list1
    if a_str == ' ':
        return list1
    d = 0
    temp = []
    for r in range(1, my_len(a_str)+1):
        if a_str[d:r] == ' ':
            temp.append(r-1)
        d +=1
    t = 0
    for y in temp:
        if a_str[t:y] != '':
            list1.append(a_str[t:y])
        t = y +1
    if a_str[(temp[-1]+1):] != '':
        list1.append(a_str[temp[-1]+1:])
    return list1

assert my_split("") == []
assert my_split(" ") == []
assert my_split("To be or not to be") == ['To', 'be', 'or', 'not', 'to', 'be']
assert my_split(" aardvark marmoset zebra ") == ['aardvark', 'marmoset', 'zebra']
assert my_split(" 10 201 -12 109") == ['10', '201', '-12', '109']

def my_sort(my_list):
    list1 = []
    if my_list == []:
        return []
    if my_list == ():
        return []
    t = []
    for u in my_list:
        t.append(u)
    while t != []:
        r = min(t)
        list1.append(r)
        t.remove(r)
    return list1

assert my_sort([]) == []
assert my_sort((5, 9, 1)) == [1, 5, 9]
assert my_sort((-1, -5, -8)) == [-8, -5, -1]

print('All good!')