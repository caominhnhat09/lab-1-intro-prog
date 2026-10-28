n = int(input('Input n: '))
each_row = ''
for r in range(n):
    each_row = ''
    for c in range(n):
        if r == 0 or r == n - 1 or c == 0 or c == n-1:
            each_row = each_row + '#'
        elif r == c or r + c == n - 1:
            each_row = each_row + '*'
        else:
            each_row = each_row + '.'
    print(each_row)
    


