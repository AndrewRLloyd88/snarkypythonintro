# Final solution to the Bill Splitter exercise

subtotal = float(input('What is the subtotal of your bill?: '))

tax_rate = 0.14

tip_percent = int(input('What percentage would you like to tip?: '))

# If the tip is negative, we have an error
if tip_percent < 0:
  print('Error: tip cannot be negative. Please restart the program.')
  exit()

# If tip is very large, ask if they're sure
if tip_percent >= 100:
  yes_or_no = input('Your tip is very large. Are you sure? (yes/no): ')
  if yes_or_no == 'yes':
    print('Continuing with tip of: ' + str(tip_percent))
  else:
    tip_percent = 20
    print('Using a more reasonable tip of ' + str(tip_percent) + ' percent')

num_people = int(input('How many people are splitting the bill?: '))

# Calculate each person's contribution
contributions = []
for i in range(0, num_people):
  percent_contributing = float(input('What percent is person ' + str(i + 1) + ' contributing?: '))
  person_subtotal = subtotal * percent_contributing
  tax = person_subtotal * tax_rate
  tip = person_subtotal * tip_percent / 100
  person_total = person_subtotal + tax + tip
  person_total = round(person_total, 2)
  contributions.append(person_total)

# Print out each person's total and the net total
net_total = 0
person_num = 1
for person_total in contributions:
  print('Person ' + str(person_num) + ' owes: $' + str(person_total))
  net_total = net_total + person_total
  person_num = person_num + 1

net_total = round(net_total, 2)
print('The net total is: $' + str(net_total))