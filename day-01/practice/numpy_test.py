# import numpy

from numpy import *


#val = array([1,2,3,4,1.1,'a']) #we didnt use typcode here

#val = array([1,2,3], float)

#val = linspace(10,20,11)                  #arithmetic progression (divide 10 to 20 in 5 parts or 11 parts)

val = arange(10,20,2) #u can use this to make diff of 2

#val = logspace(10,20,2) #output is 10^2 anbd 20^2

#val = zeros(10) # output is 0.0 0.0 up to 10 times
# val = ones(2) #output 1.0 1.0

#val = full(10,5) # output is 10 times 5


for x in val :
    print(x)

# print multidimensionl array

zero = array(10)
print(zero)

one = array([1,2,3,4,])
print(one)


two = array([[1,2,3], [4,5,6], [7,8,9]])
print(two)


three = array([[[1,2],[3,4], [5,6],[7,8]]])
print(three)