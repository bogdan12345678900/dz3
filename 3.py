def list1(lst):
    def a(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(1 for num in lst if a(num))


lst = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Кількість простих чисел у списку: {list1(lst)}")
