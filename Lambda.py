# square = lambda x : x**2
# print(square(6))

# check_even = lambda x : "Even" if x % 2 == 0 else "Odd"
# print(check_even(10))

# l = list(map(int, input("enter numbers: ").split(",")))
# doubled = map(lambda x : x ** 2, l)
# print(l)
# print(list(doubled))

l = list(map(int, input("enter numbers: ").split(",")))
even = filter(lambda x : x % 2 == 0, l)
print(l)
print(list(even))
