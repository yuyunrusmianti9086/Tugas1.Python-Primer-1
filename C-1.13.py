# pseudocode
# funtion(list):
#     reversed_list = []
#     for i in range(0, reversed_list_length):
#         append list[i] to reversed_list
#     return reversed_list
# append mengurutkan dari belakang
# prepend mengurutkan dari depan
def reverse_list_of_integers(list):
    reversed_array=[]
    for i in range(0, len(list)):
        reversed_array.append(list[len(list)-i-1])
    return reversed_array
print(reverse_list_of_integers([5,6,7,8,9,10]))
