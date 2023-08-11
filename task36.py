def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        sp = []
        for j in range(1, num_columns + 1):
            sp.append(str(operation(i, j)))
        print(' '.join(f'{k:<3}' for k in sp))

print_operation_table(lambda x, y: x * y)