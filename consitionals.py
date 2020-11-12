# We often need to make decision based certain factors.
# Imagine checking if someone is allowed to ride a rollercoaster:
#
# Are they older than 18?
#   If so, then they can definitely ride it

# In Python
print('Can you ride this rollercoaster?')
age = int(input('What is your age?: '))

if age > 18:
  print('Definitely!')

# Syntax:
# if condition:
#   Do stuff
#   Do some more stuff (can have many lines)

# Else statements
print('Can you ride this rollercoaster?')
age = int(input('What is your age?: '))

if age > 18:
  print('Definitely!')
else:
  print('Sorry kid. Come back in a couple years.')

# Elif (and nested conditionals)
print('Can you ride this rollercoaster?')
age = int(input('What is your age?: '))

if age > 18:
  print('Definitely!')
elif age > 12:
  height = int(input('What is your height in inches?: '))
  if height >= 48:
    print('Okay, you can ride it.')
  else:
    print('Sorry kid. Come back after you grow.')
else:
  print('Sorry kid. Come back in a couple years.')

  # Let's improve out bill splitter so that it  does different things 
  # based on the value of the tip