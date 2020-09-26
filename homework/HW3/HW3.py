#
n = 10
order = [1,2,3]
num = [[1], [2], [3]]
print(num)
for i in range(n):
    temp = []
    for j in num:
        for k in order:
            j.append(k)
            temp.append(j)
    num = temp
print(num.shape)