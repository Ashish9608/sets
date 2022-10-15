# set

set1 = {10,20,30,40}
print(len(set1))

set2 = {'orange', 30, 'lemon', 50, 60}
print(set2)


# Access the items in a set

mySet = {20,30,30}

for x in mySet:
    print(x)

print(200 in mySet)


# Add items

myset = {'lion', 'tiger', 'zebra'}

myset.add(10)
myset.add('abc')

print(myset)

# Add items from one set to another

set4 = {10,20,30,40}
set5 = {50,60}
list1 =[50,60]

set4.update(list1)

print(set4)


# Remove Item

set5 = {10,20,30,40,50}

set5.remove(20)
set5.discard(30)

print(set5)


# Joining the sets


#join using union
set6 = {10,20,30,40}
set7 = {'a', 'b', 'c', 'd'}


set8 = set6.union(set7)
set6.update(set7)         # modifying set 6
set7.update(set6)         # modifying set 7


print(set8)
print(set6)
print(set7)


#join using intersection

a = {10,20,30,40,50}
b = {40,50,60,70}
a.intersection_update(b)   #modifying the set a
b.intersection_update(a)   #modifying the set b
c = a.intersection(b)

print(a)
print(b)
print(c)




x = {10,20,50,}
y = {40,50,60,}

x.symmetric_difference_update(y)                     

z = x.symmetric_difference(y)

print(x)
print(z)




