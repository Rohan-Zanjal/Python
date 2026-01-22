# 1. To add (insert) number in position 1 in array, to insert in last position of whole array and 
# replace value in 2nd position


from array import *

arr = array('i',[1,2,3,4,5,6,7])

arr.insert(1,89)
arr.append(100) #to insert in last position of whole array
arr[2] = 200 #replace value in 2nd position

for i in range(0, len(arr)):
    print(arr[i], end=',')

print('\n',"-------------------------------------------------------------------------------------------------------------------", '\n')

#-------------------------------------------------------------------------------------------------------------------

# 2. Copy array

copyArray = array(arr.typecode , (x*2 for x in arr))

for i in range(0, len(copyArray)):
    print(copyArray[i], end=',')


print('\n',"-------------------------------------------------------------------------------------------------------------------", '\n')

#-------------------------------------------------------------------------------------------------------------------

# 3. Delete element in array

copyArray.pop(3)
copyArray.remove(200) #if you dont know the index but you know the value

for i in range(0, len(copyArray)):
    print(copyArray[i], end=',')

print('\n',"-------------------------------------------------------------------------------------------------------------------", '\n')

#-------------------------------------------------------------------------------------------------------------------

# 4. If I want a part of array or I want to reverse a array.

# eg:-  a = val[start index : end index]

#abc = arr[1 : -2]

abc = arr[::-1] #for reverse

for i in range(0, len(abc)):
    print(abc[i], end=',')

print('\n',"-------------------------------------------------------------------------------------------------------------------", '\n')

#-------------------------------------------------------------------------------------------------------------------

# 5. Take input from users

val = array('i', [])
n = int(input("Enter a nmber"))

for i in range (0, n):
    val.append(int(input("Enter the next input")))

for x in val:
    print(x, end=" ")


print('\n',"-------------------------------------------------------------------------------------------------------------------", '\n')

#-------------------------------------------------------------------------------------------------------------------
# 6. Search element in array

i = arr.index(100)
print(i)