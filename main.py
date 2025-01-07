def add(first, second):
    return first + second
def minus(first, second):
    return first - second
def multi(first, second):
    return first * second
def divide(first, second):
    return first / second
select = int(input("Select operation: \n1. Add(=): \n2. Minus(-): \n3. Multiply(*): \n4. Divide(/): "))
first = int(input("Write first expression: "))
second = int(input("Write second expression: "))
if select == 1:
    print("Results: ", add(first, second))
elif select == 2:
    print("Results: ", minus(first, second))
elif select == 3:
    print("Results: ", multi(first, second))
elif select == 4:
    print("Results: ", divide(first, second))
else:
    print("Currently only basic math operations are available")