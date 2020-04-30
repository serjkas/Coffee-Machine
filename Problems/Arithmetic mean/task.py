numbers = [int(x) for x in input().split()]
sum = 0
iter = 0
for number in numbers:
    sum += int(number)
    iter += 1

print(sum/iter)
