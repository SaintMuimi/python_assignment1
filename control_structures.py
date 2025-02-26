num = int(input("Enter an integer: "))
def classify(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

print(classify(num))


even = [num for num in range(1, 51) if num % 2 == 0]
print("List of even numbers from 1 to 50:", even)

count = 10
while count > 0:
    print(count)
    count -= 1


