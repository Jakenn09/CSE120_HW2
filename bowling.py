scores = [[8, 1], [5, 3], [3, 5], [8, 1], [7, 1], [1, 0], [9, 0], [5, 0], [6, 0], [8, 1, 0]]
sum = 0
for i in range(10):
    for j in range(2):
        sum = sum + (scores[i][j])
print(sum)