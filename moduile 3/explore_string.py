name = 'sakib\'s khan'   #escape
name2 = "sakib khan"
#multilinr string
name3 = """"
    sakib khan   
    numner one
"""

print(name)
#string is a sequance od charectures
for char in name2:
    print(char)
    
print(name2[3])    
#mutable means changeable
#imutable means yiu can not change it
# name2[0] ='R'
print(name2)
if 'khan' in name2:
    print('exsists')

print(name2.upper())    

