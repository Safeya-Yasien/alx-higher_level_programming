#!/usr/bin/python3
def common_elements(set_1, set_2):
    comman_list = []
    for i in set_1:
        for j in set_2:
            if i == j:
                comman_list.append(i)
    return (comman_list)
