test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]

def pos_sum(arr):
    pos_count = 0
    neg_sum = 0
    for n in arr:
        if(n<0):
            neg_sum += n
        elif(n>0):
            pos_count += 1
    return([pos_count,neg_sum])

print(pos_sum(test_arr))