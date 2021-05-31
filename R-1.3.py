def minmax(data):
    smallest = largest = data[0]
    for entry in data:
        if smallest > entry:
            smallest = entry
        if largest < entry:
            largest = entry
    return (smallest, largest)
print(minmax([5,4,3,2,1,1,-1,-2,-3,-4]))
