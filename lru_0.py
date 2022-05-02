''' Imports : Doubly-Linked Lists '''
from pyllist import dllist, dllistnode

# 12

''' Variables '''
lst = dllist([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
reference_string = []
page_faults = 0
page_frames = []
page_frames_length = 3

''' Modify this value to display a specific page fault '''
seek_page_fault = 110

''' Parse Information '''
text_file = open("data.txt", "r")
reference_string = text_file.read().split('  ')
reference_string = list(map(int, reference_string))

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
    elif len(page_frames) < page_frames_length:
        page_frames.append(item)
        page_faults += 1
        assert(len(page_frames) <= 3)
    else:
        if page_faults == seek_page_fault - 1:
            print(f'{page_frames}')
        val = lst.nodeat(page_frames_length).value
        index = page_frames.index(val)
        page_frames[index] = item
        page_faults += 1
    if page_faults == seek_page_fault:
        print(f'{page_frames}')
        print(f'{item} replaced {val}')

print(f'pgfaults -> {page_faults}')
