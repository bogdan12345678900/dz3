def power_list(lst, power):
 result = []
 for x in lst:
   result.append(x**power)
 return result


num = [1, 2, 3, 4]
print(power_list(num, 3))