def unique_in_order(iter):
    prev = ""
    out_list = []
    for i in iter:
        if(i != prev):
            out_list.append(i)
        prev = i
    print(out_list)
    return(out_list)

unique_in_order('AAAABBBCCDAABBB')
unique_in_order('ABBCcAD')        
unique_in_order([1,2,2,3,3]) 