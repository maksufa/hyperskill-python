summary = {
'Bubblegum':202,
'Toffee':118,
'Ice cream':2250,
'Milk chocolate':1680,
'Doughnut':1075,
'Pancake':80
}

print('Earned amount:')
for product, price in summary.items():
    print(f'{product}: ${price}')

print()
income = sum(summary.values())
print(f'Income: ${income}')

staff_expenses = int(input('Staff expenses: '))
other_expenses = int(input('Other expenses: '))

print(f'Net income: ${income - staff_expenses - other_expenses}')