numbers = []
def even():
    for num in range(1,51):
        if num % 2 == 0:
            numbers.append(num)
    print(numbers)
    return numbers
even()