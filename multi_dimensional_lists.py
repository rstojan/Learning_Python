mult_table = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]

for row in mult_table:
    for i, cell in enumerate(row):
        if i < len(mult_table[0]) -1:
            print(cell, '|',end=" ")
        else:
            print(cell)
