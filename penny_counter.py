def number_of_pennies(dollars, pennies=0):
    pennies_in_dollars = dollars * 100
    return pennies_in_dollars + pennies

print(number_of_pennies(5, 6)) # Should print 506
print(number_of_pennies(4))    # Should print 400