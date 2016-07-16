def biggest_num(input_list):
    biggest_num_list = [0]
    for input_num in input_list:
        for index,item in enumerate(biggest_num_list):
            if has_bigger_digits(input_num,item):
                biggest_num_list.insert(index,input_num)
                # print '\n'
                break

    print biggest_num_list[:len(biggest_num_list)-1]


def has_bigger_digits(input_num,item):
    if get_digit(input_num,0) > get_digit(item,0):
        return True
    if get_digit(input_num,0) == get_digit(item,0):
        # print input_num,item
        return has_bigger_digits(int(str(input_num)[1:]),int(str(item)[1:]))


def get_digit(num,pos):
    return int(str(num)[pos])


biggest_num([18,90,20,25,30,40,50])
