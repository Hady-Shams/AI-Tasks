# Task[1]:  Remove element occurred more than one time #

list = [5, 1, 2, 3, '1', True, 5, 1.0]

for i in list:
    if i == 1:
        list.remove(i)
    
print(list)
##################################################################

# Task[2]:  Print ASCII of a character #

x = 'a'
print(ord(x))
x = 97
print(chr(x))
##################################################################

# Task[3]:  Take two numbers from user and operation then print the result #

n1 = int(input('First num: '))
op = str(input('Operation: '))
n2 = int(input('Second num: '))

if op == '+':
    r = n1 + n2
elif op == '-':
    r = n1 - n2
elif op == '*':
    r = n1 * n2
elif op == '/':
    r = n1 / n2
    
print('Result = ', r)




