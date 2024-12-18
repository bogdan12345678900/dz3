def remove_el(lst, num_remove):
    org_lst = len(lst)
    lst = [num for num in lst if num != num_remove]
    removed_count = org_lst - len(lst)
    return removed_count, lst


e_list = [1, 2, 3, 4, 5, 3, 6, 3, 7]
num_remove = 3
a, b = remove_el(e_list, num_remove)
print(f"Number of items removed: {a}")
print(f"Updated list: {b}")
