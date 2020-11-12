# a = 1
# print(a)



subtotal = float(input('what is the subtotal?: '))
tax_rate = 0.14
tax = subtotal * tax_rate
total = subtotal + tax
total = round(total, 2)
print(total)
# 20.20 * 0.14 + 20.20