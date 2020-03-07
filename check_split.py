def split_check(total, num_diners, tip_rate=0.15, tax_rate = 0.09):
    cost_divided_by_person = (total + (total * tip_rate) + (total * tax_rate)) / num_diners
    return round(cost_divided_by_person, 2)

total = float(input('Enter bill total:\n'))
num_diners = int(input('Enter number of diners:\n'))

print('Cost per diner:', split_check(total, num_diners, tax_rate = 0.075))
