list_1 = ['a','b','c','d']
list_2 = [1,2,3]
# op = {'a':1, 'b':2, 'c':3, 'd':0}

def dict_generator(list_1,list_2):
    dict = {}
    for i in range(len(list_1)):
        if i < (len(list_2)):
            dict[list_1[i]] = list_2[i]
        else:
            dict[list_1[i]] = 0
    return dict

    # for i , j in list_1 , list_2:
    #     dict[i] = j
    #  return dict

print(dict_generator(list_1,list_2))