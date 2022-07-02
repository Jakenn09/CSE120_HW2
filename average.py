def average(arr):
        return sum(arr) / len(arr)

arr = []
total = int(input("How many numbers would you like to input? "))
for i in range(total):
    x = int(input("Enter Number: "))
    arr.append(x)
print("The average is: ", average(arr))