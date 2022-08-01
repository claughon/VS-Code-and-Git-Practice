list_a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list_c =[1,12,3,5,16,8,9,12,4]
def is_consecutive(a_list):
    for ind, number in enumerate(a_list):
        if ind == 0:
            continue
        else:
            if a_list[ind] == a_list[ind-1] + 1:
                continue
            else:
                print(False)
                return(True)
                break            
    print(True)


is_consecutive(list_c) 
is_consecutive(list_a)