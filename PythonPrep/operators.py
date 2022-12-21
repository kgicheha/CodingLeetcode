'''
Given the meal price (base cost of a meal),
tip percent (the percentage of the meal price being added as tip),
and tax percent (the percentage of the meal price being added as tax)
for a meal, find and print the meal's total cost.
Round the result to the nearest integer.

Example
meal cost = 100
tip percent = 15
tax percent = 8
A tip of 15% of 100 = 15, and taxes will be 8% * 100 = 8
result will be 123
'''

'''
GIVEN: meal cost, tip percent, tax percent

STEPS:
    calc total tip
        total_tip = (tip_percent/100) * meal_cost
    calc total tax
       total_tax = (tax_percent/100) * meal_cost
    total cost = round(meal_cost + total_tip + total_tax)

RESULT: print the total cost of meal(rounded)

'''
def operator(meal_cost, tip_percent, tax_percent):
    total_tip = (tip_percent/100) * meal_cost
    total_tax = (tax_percent/100) * meal_cost
    total_cost = round(meal_cost + total_tip + total_tax)
    print(total_cost)

operator(100, 15,8)
operator(12.00, 20,8)