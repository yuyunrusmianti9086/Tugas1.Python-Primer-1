def odd_product_pair(data):
    data = set(data)
    for i in data:
        for j in data:
            if i == j :
                continue
        if i*j % 2 == 1:
            return True
    return False
print(odd_product_pair([1,3,2,4,6]))
