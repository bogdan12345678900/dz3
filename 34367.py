def sum_num(lst):
    a = 1
    for num in lst:
        a *= num
    return a


lst = [1, 2, 3, 4, 5]
print(f"List item output: {sum_num(lst)}")
