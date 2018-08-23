def exists(n, list1):
    i = 0
    while i <= len(list1) - 1:
        if n == list1[i] :
            return True
        i = i + 1

    return False

# print(exists([3, 5, 6], 5))

def filt(r_list, f_list):
    i = 0
    result = []
    while i <= len(r_list) - 1:
        if not exists(r_list[i], f_list):
            result.append(r_list[i])
        i = i + 1
    return result



print(filt([7, 5, 3, 2], [9, 5, 3,]))

# // filter([7, 5, 3, 2], [9, 5, 3]) y me retorna [7, 2]7
