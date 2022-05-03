''' Imports : Doubly-Linked Lists '''
from pyllist import dllist, dllistnode

''' USER CHANGE DATA '''
lst = dllist([0, 1, 2, 3, 4, 5, 6, 7])
len_pgframes = 3
desired_page_fault = 9
''' END USER CHANGE DATA '''

''' Variables '''
reference_string = [7, 2, 3, 1, 2, 5, 3, 4, 6, 7, 7, 1, 0, 5, 4, 6, 2, 3, 0, 1]
page_faults = 0
page_frames = []

# ''' Parse Information '''
# text_file = open("data.txt", "r")
# reference_string = text_file.read().split('  ')
# reference_string = list(map(int, reference_string))

''' LRU '''
for item in reference_string:
    # modify stack
    for node in lst.iternodes():
        if node.value == item:
            lst.remove(node)
            lst.appendleft(item)
            break
    # page replacement
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
