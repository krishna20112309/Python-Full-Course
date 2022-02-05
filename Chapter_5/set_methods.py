#Creating an empty set
b=set()
print(type(b))

#Adding the values to an empty set
b.add(4)
b.add(5)
b.add((4,5,6,8)) # We can add tuple in set 
# b.add([4,5,6,8]) # We cannot add List in set because it is not Hashable 
# b.add({4:5}) Cannot add dictionary because it ia not hashable
print(b)
print(len(b)) # Prints the length of the set
b.remove(5)   # Remove 5 from the set
# b.remove(15)  # Throws an error because 15 is not present in the set
print(b)

# print(b.pop())
# print(b)
# print(b.clear())  # Empties the set

# print(b.union({12,25,36}))
print(b.intersection({4,26}))