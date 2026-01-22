# if we have to use array in python the we have to import array module or numpy


#import array as arr
from array import *

val = array('i', [1,2,3,4,5,6,7]) #or arr.array('i', [1,2])

for i in range(0, 6):
    print(val[i])

print('\n')

print(",".join(map(str, val))) #if you dont want ',' after end of the line  

print('\n')
for x in val:
    print(x, end=",")

print('\n')
    

print('\n',"Length is : ", len(val))
print('\n', "typecode is : ", val.typecode)

print('\n')


#to reverse array
val.reverse()
for i in range (0,len(val)):
    print(val[i], end=" ")

#---------------------------------------------------------------------------------------------------------------

