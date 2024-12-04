# Get data
arr1, arr2 = [], []

with open('data.txt', 'r') as file:
    for line in file.readlines():
        value1, value2 = (int(number) for number in line.split())
        # get from list, appears to be fixed number lengths
        arr1.append(value1)
        arr2.append(value2)

arr1.sort()
arr2.sort()
length = len(arr1)

# part 1
arr3 = []
for i in length:
      arr3.append(abs(arr2[i]-arr1[i]))

print('part 1', sum(arr3))

# part 2

arr4 = []
for i in arr1:
     arr4.append(len([y for y, x in enumerate(arr2) if x == i])*i)

print('part 2', sum(arr4))