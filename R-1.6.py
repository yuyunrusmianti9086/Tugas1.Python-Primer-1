def squared_odd_sum(n):
    sum = 0
    for angka in range(n):
        if angka%2 == 0:
            continue
        sum = sum + angka**2
    return sum
print(squared_odd_sum(7))
