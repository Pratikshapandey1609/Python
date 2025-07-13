"""
[expression for item in iterable if condition]

expression = x * 2

# squares = []
# for i in range(1,11):
#     squares.append(i ** 2)
#     print(squares)
"""

squares = [1 ** 2 for i in range(1,11) if i%2 == 0]
print(squares)
