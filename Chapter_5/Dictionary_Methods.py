myDict={
    "Fast": "In a Quick Manner",
    "Krishna": "A coder",
    "marks": [1, 2, 5],
    "anotherdict":{'Krishna':'Player'},
    1:2
}
print(list(myDict.keys()))  #Prints the keys of the Dictionary
print(myDict.values())   #Print the values of Dictionary
print(myDict.items())   #Print the (Key, Value) for all contents of the dictionary
print(myDict)
updateDict={
    "Lovish": "friends",
    "Shubham": "Friends"
}
myDict.update(updateDict) # Updates the Dictionary by adding key-value pairs from updateDics
print(myDict)

print(myDict.get("Krishna"))   # Print value associated with key Krishna

print(myDict["Krishna"])     # Print value associated with key Krishna

print(myDict.get("Krishna2"))   # Returns none as Krishna2 is not present in the dictionary

# print(myDict["Krishna2"])     # throws an error as Krishna2 is not present in the dictionary

