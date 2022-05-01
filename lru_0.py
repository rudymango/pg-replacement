''' Imports : Doubly-Linked Lists '''
from pyllist import dllist, dllistnode

''' Variables '''
lst = dllist([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
reference_string = []
page_faults = 0
page_frames = []
page_frames_length = 3
count = 0

''' Parse Information '''
text_file = open("data.txt", "r")
reference_string = text_file.read().split('  ')
reference_string = list(map(int, reference_string))

''' LRU '''
for item in reference_string:
    count += 1
    if page_faults == 109:
        print(lst)
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
    elif len(page_frames) < page_frames_length:
        page_frames.append(item)
        page_faults += 1
        assert(len(page_frames) <= 3)
    else:
        if page_faults == 109:
            print(f'{page_frames}')
        val = lst.nodeat(page_frames_length).value
        index = page_frames.index(val)
        page_frames[index] = item
        page_faults += 1
    if page_faults == 110:
        print(lst)
        print(f'{item} replaced {val} \t {page_frames}')


# print(f'{count}')
# print(f'{page_faults}')
