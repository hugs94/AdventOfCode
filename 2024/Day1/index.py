# Get data

arr1 = []
arr2 = []

with open('data.txt', 'r') as file:
    for i in range(1000):
        data = file.readline()
        # get from list, appears to be fixed number lengths
        arr1.append(int(data[0:5]))
        arr2.append(int(data[8:13]))
# basically lazy, surely you could optimize a sort in place or something while looping initially.
arr1 = sorted(arr1)
arr2 = sorted(arr2)

# part 1
arr3 = []

for i in range(1000):
      arr3.append(abs(arr2[i]-arr1[i]))

print('part 1', sum(arr3))

# part 2

arr4 = []
for i in arr1:
     arr4.append(len([y for y, x in enumerate(arr2) if x == i])*i)

print('part 2', sum(arr4))