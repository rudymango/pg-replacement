''' Imports : Doubly-Linked Lists '''
from pyllist import dllist, dllistnode

''' USER CHANGE DATA '''
lst = dllist([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # make sure that this linked list includes all pages in reference_string
len_pgframes = 3                        # set amount of frames
desired_page_fault = 110                  # 0 for no pgfaults
parse = 1                               # 1 = parse from data.txt
''' END USER CHANGE DATA '''

page_faults = 0
page_frames = []

if parse == 1:
    text_file = open("data.txt", "r")
    reference_string = text_file.read().split('  ')
    reference_string = list(map(int, reference_string))
else:
    reference_string = [7, 2, 3, 1, 2, 5, 3, 4, 6, 7, 7, 1, 0, 5, 4, 6, 2, 3, 0, 1]

for item in reference_string:
    for node in lst.iternodes():
        if node.value == item:
            lst.remove(node)
            lst.appendleft(item)
            break
    exists = item in page_frames
    if exists:
        continue
    elif len(page_frames) < len_pgframes:
        page_frames.append(item)
        page_faults += 1
        assert(len(page_frames) <= 3)
    else:
        # if page_faults == desired_page_fault - 1:
        #     print(f'{page_frames}')
        val = lst.nodeat(len_pgframes).value
        index = page_frames.index(val)
        page_frames[index] = item
        page_faults += 1
    if page_faults == desired_page_fault:
        # print(f'{page_frames}')
        print(f'{item} replaced {val}')

print(f'pgfaults -> {page_faults}')
