from random import randrange
def pilih_data(data):
    x = randrange(0 ,len(data))
    return data[x]
print(pilih_data([3,4,5,1,2]))
