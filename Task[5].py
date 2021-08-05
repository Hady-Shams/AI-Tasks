### Task [1] : implement unordered set using list ###

us = []
def add(element):
    f = 0
    for i in range(len(us)):
        if element == us[i]:
            f += 1
    if f == 0:
        us.append(element)

add(5)
add(3)
add(1)
add(56)
add(5)
add(566)
add(56)

print(us)

print('#' * 50)
##################################################

### Task [2] : implement binary search so that when searching return either the right index or not found ###

lis = [3, 1, 22, 4, 90, 11, 3, 5]
def bs(lis, element):
    lis = sorted(lis)
    first = 0
    last = len(lis) - 1
    while first <= last:
        mid = (first + last) // 2   ## Used "//" not "/" to be integer
        if element == lis[mid]:
            return lis, mid
        elif element < lis[mid]:
            last = mid - 1
        else:               # element > l[mid]
            first = mid + 1
    return 'Not found :('

print(bs(lis, 900))

print('#' * 50)
##################################################


        