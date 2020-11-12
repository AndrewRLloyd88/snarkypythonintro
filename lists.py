# Without lists, individual and unrelated variables
# (imagine if you had hundreds of names)
first_person = 'Mal'
second_person = 'Zoe'
third_person = 'Wash'
fourth_person = 'Jayne'
fifth_person = 'Kaylee'

# Using lists, a data structure that contains many values
people = ['Mal', 'Zoe', 'Wash', 'Jayne', 'Kaylee']

# List creation
empty_list = []            # Square brackets
small_list = [2.3, 1.0]    # List elements separated by commas
large_animals = ['African Elephant', 'Asian Elephant', 'White Rhinoceros',
                 'Hippopotamus', 'Gaur', 'Giraffe', 'Walrus', 'Black Rhinoceros', 
                 'Saltwater Crocodile', 'Water Buffalo']

# Accessing elements in a list by their index (i.e. their position)
a = large_animals[0]    # 1st element
b = large_animals[5]    # 6th element
c = large_animals[-1]   # 1st element starting from the end (i.e. last element)
some_index = 6
d = large_animals[some_index]    # Can access using variables as well

# Accessing indices (positions) by their value
a = large_animals.index('Black Rhinoceros')

# Accessing slices (chunks) of the list
a = large_animals[0:3]    # 1st to 3rd element (indices 0, 1, and 2)

# Modifying elements
large_animals[3] = 'Penguin'

# Deleting elements
del large_animals[3]

# List size
b = len(a)    # Number of elements in a

# Extending lists
large_animals.append('Tiger')        # Add an element to the list
d = large_animals + ['Wolf', 'Dog']  # Join two lists

# Lists within lists
animal_kingdom = [
  ['Elephant', 'Tiger', 'Dog'], 
  ['Whale', 'Dolphin', 'Shark', 'Eel'],
  ['Eagle', 'Robin']
]
water_animals = animal_kingdom[1]    # 1st list
biggest_bird = animal_kingdom[-1][0] # Last list, first element

# Treating strings like lists
a = 'this is really just a list of symbols called characters'
b = a[5:7]

# Splitting strings into lists
b = a.split(' ')       # A list of words (splitting the string by ' ')
b = a.split('symbols') # Splitting by a substring