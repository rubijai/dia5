import matplotlib.pyplot as plt

def maxv(nlist):
    max_value = nlist[0]
    for x in nlist[1:]:
        if x > max_value:
            max_value = x
    return max_value

a = [5,6,-10,-12,42,1]
print(maxv(a))

def plt_list_data(x,y,plt_docu):
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Test Plot')
    plt.savefig('plot1.png')

plt_docu = ['X', 'Y', 'Test Plot', 'plot1.png']
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(plt_list_data(x,y,plt_docu))


'''Given the width and height of a rectangle as inputs, complete 
the function named perim that will compute the perimeter of the rectangle.'''
def perim(width,height):
    return 2*width + 2*height

print(perim(10,20))


'''Given a numerical list as an input, you will complete the function 
named 'listsum' that will return the sum of the values contained 
in the list. Your function must use a for loop in order to solve this problem.'''
def listsum(indata):
    sum = 0
    for x in indata:
        sum += x
    return sum

print(listsum([1,2,3,4,5]))


'''Given a numerical list and a value as inputs, complete the function 
findval that will search to see if the input value is in the list. 
If the value is found, your function should return the index 
of the first occurrence. If the value is not found, findval 
should return a value of -1.'''

def findval(inlist, inval):
    if inval in inlist:
        x = inlist.index(inval)
    else:
        x = -1

    return x
print(findval([1,2,3,4,5,6,7,8,9],40))


'''Given a numerical list as an input, complete the function named findmin 
that will find the minimum of the set of values contained in the list.'''

def findmin(inlist):
    minval = inlist[0]
    for v in inlist[1:]:
        if minval > v:
            minval = v
    return minval

print(findmin([-3, 4, 3, 0, -100, 2]))





'''Complete the function named circarea that, given an input radius,
 will compute the area of a circle. You must import the math 
 module and use the value of pi in that module.'''

import math
def circarea(r):
    return math.pow(r, 2)*math.pi






'''Complete the function named revlist that will take an input 
list and return the list with its elements in reverse order. 
For instance, for the input list [1,2,3,4,5], revlist should return [5,4,3,2,1].'''

def revlist(inlist):
    revlist = inlist[-1::-1]
    return revlist
print(revlist([1,2,3,4,5]))





'''Complete the function named reorder that will take an input list 
and return a list that contains the even indexed elements followed 
by the odd-indexed elements. For example, if the input list is
[10,11,12,13,14,15,16,17,18,19], the returned list should be 
[10,12,14,16,18,11,13,15,17,19].'''

def reorder(inlist):
    z = []
    x = inlist[::2]
    z.extend(x)
    y = inlist[1::2]
    z.extend(y)
    return z
print(reorder([10,11,12,13,14,15,16,17,18,19]))

'''Assume that two input angles A and B given in degrees, complete the function 
named anglesumtest that will compare cos(A+B) to its equivalent trigonometric identity

cos(A+B)=cos(A)cos(B)-sin(A)sin(B).

The function input variables A and B are angles in degrees. Your function output 
should be either True or False depending on whether or not the above identity 
is correct. Your function should perform the following steps:

Convert the input angles from degrees to radians using the math.radians method.
Compute cos(A+B)
Compute cos(A)cos(B)-sin(A)sin(B)
Apply the math.fabs method to compute the absolute value of the difference 
between the values computed in steps 2 and 3.
If the quantity in step 4 is less than 1e-15, return True; otherwise, return False.'''
import math
def anglesumtest(A,B):
    X = math.cos(math.radians(A)+math.radians(B))
    Y = math.cos(math.radians(A))*math.cos(math.radians(B))
    W = math.sin(math.radians(A))*math.sin(math.radians(B))
    R = Y-W
    if math.fabs(X-R) < 1e-15:
        return True
    else:
        return False
print((anglesumtest(30,60)))
'''Complete the function named coinflip to use the random method 
from the random module, where N is the number of coin flips.

Your function should:

Initialize a variable nheads to 0, which will keep track of the number of heads
Use a 'for' loop that will execute N times to do the following:
Generate a random number x between 0 and 1 using the random.random method
If 0<=x<=0.5, increment nheads
After the 'for' loop, compute the empirical probability: prob_heads=nheads/N
Using the math.fabs method from the math module, compute the absolute 
value of the difference: e=|prob_heads-0.5|.
If e<0.01, then return True; otherwise, return False
You will need to import both the random and math modules to solve this problem. 
In order to ensure a True result (that is, a 50% probability of heads after N flips), 
you should use an input value of N>=100000.'''

import math
import random
def coinflip(N):
  nheads=0
  for i in range(N):
      x = random.random()
      if  0<=x<=0.5:
          nheads += 1
  prob_heads = nheads/N
  e = math.fabs(prob_heads - 0.5)
  return e < 0.01

print(coinflip(1000))

#This expression can be used to approximate pi:
#π=2V
#where
#V=sqrt(2).sqrt(2+sqrt(2)).sqrt(2+sqrt(2+sqrt(2))).sqrt(2+sqrt(2+sqrt(2+sqrt(2)))).....



#Complete the function pi_approx, which should take a positive integer input N and compute the above product for V
#by iterating N square root terms in the product.
#Given N, use a 'for' loop to compute N products for the square root terms in V
#After the loop is finished, compute: pi_est=2/V
#Compute the absolute value of the difference between pi_est and math.pi using the math.fabs method
#If the error value computed in step 3 is less than 1e-7, return True; otherwise, return False
#The estimate should work if N>=100.

#You will need the math module for this question.

def pi_approx(N):
    x=math.sqrt(2)
    y = x/2
    for i in range(N):
        x=math.sqrt(2+x)
        y *= x/2
        print(x, y)
    pi_est = 2/y
    e = math.fabs(pi_est-math.pi)
    print(pi_est)
    return e < 1e-7
print(pi_approx(2))

def factoria(n):
    print(f'n={n}')
    if n == 0:
        return 1
    else:
        print(f'n={n}, n-1={n-1}, n*factoria(n-1)={n*factoria(n-1)}')
        return n*factoria(n-1)
print(factoria(7))
n = 7
res = 1
for i in range(1,n+1):
    res *= i
print(res)

x = 2**0.5
print(x)
y = (2+x)**0.5
print(y)
for i in range(10):
    y = (2+y)**0.5
    print(y)
