#yield keyword
def count_down(num):
    while num > 0:
        yield num
        num -= 1

# using the genrator
for number in count_down(5):
    print(number)