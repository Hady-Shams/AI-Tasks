## Constant variables ##

CONST_pi = 22 / 7
CONST_sum_factor = 0
CONST_mul_factor = 1
CONST_cal_name = 'Hady Shams'

## Functions

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
   return n1 * n2

def div(n1, n2):
    return n1 / n2

def fact(n): 
    if n==1 or n==0:       
        return 1    
    else:       
        return n * fact(n - 1)