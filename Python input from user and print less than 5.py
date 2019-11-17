a = [1,1,2,3,4,8,13,21,34,55,89]
#now run a loop to traverse through the list
def print_less_than_five():
for i in range(len(a)):
if a[i]<5: #checking if the element is less than 5
print(a[i]) #printing
"""
or we cound write this like
for i in a:
if i<5:
print(i)
"""
print_less_than_five()