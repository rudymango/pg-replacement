reference_string = [
1, 3, 0, 5, 6, 9, 6, 4, 1, 7, 6, 3, 0, 7, 0, 9, 3, 9, 6, 3, 7, 6, 1, 5, 0, 1, 9, 3, 5, 7, 3, 5, 2, 5, 8, 2, 6, 9, 8, 9, 6, 8, 5, 8, 6, 0, 5, 9, 0, 5, 1, 2, 7, 6, 0, 2, 0, 6, 1, 8, 2, 8, 3, 5, 0, 5, 6, 3, 6, 9, 0, 3, 5, 4, 7, 4, 0, 5, 4, 7, 4, 9, 1, 3, 7, 9, 8, 5, 8, 3, 9, 3, 4, 9, 6, 9, 1, 2, 9, 4, 7, 2, 5, 8, 6, 1, 8, 5, 8, 1, 6, 5, 9, 8, 3, 4, 7, 8, 4, 3, 0, 1, 3, 7, 0, 6, 4, 1, 2, 1, 7, 6, 8, 4, 2, 1, 5, 4, 7, 3, 7, 1, 9, 0, 4, 5, 9, 4, 9, 4, 5, 6, 0, 9, 4, 2, 5, 0, 5, 1, 6, 7, 6, 9, 1, 6, 3, 1, 4, 1, 5, 0, 3, 9, 4, 0, 6, 4, 7, 8, 1, 5, 0, 3, 2, 9, 8, 9, 8, 7, 8, 9, 4, 1, 7, 6, 1, 7, 5, 7, 8, 3, 4, 3, 9, 2, 3, 2, 0, 7, 4, 8, 1, 8, 2, 3, 1, 8, 9, 6, 0, 9, 6, 2, 1, 2, 9, 0, 7, 5, 7, 2, 7, 8, 7, 8, 0, 9, 6, 8, 1, 3, 9, 8, 0, 7, 5, 4, 7, 4, 1, 7, 3, 1, 7, 0, 9, 3, 4, 7, 9, 7, 9, 6, 9, 6, 4, 5, 9, 8, 9, 0, 4, 6, 7, 1, 4, 6, 1, 2, 1, 6, 1, 3, 0, 2, 3, 7, 0, 1, 7, 1, 5, 6, 2, 8, 3, 9, 1, 4]
queue = []
page_frames = [999, 999, 999]
page_frames_length = 3
page_faults = 0

# for loop variables
index = 0
limit = 2

# queue first three elements
for item in reference_string:
    queue.append(item)
    index += 1
    page_faults += 1
    if index > limit:
        break

page_frames = queue

# testing queue init correctly
# test_queue = [7, 0, 1]
# if queue != test_queue:
#     print(f'{queue} != {test_queue}')

# FIFO for-loop variables
index = 0

# don't ask but this needs to be in the code
exists = 7 in page_frames
#print(f'{page_frames.index(7)}')

# FIFO algorithm
for item in reference_string:
    # skip first 3 elements
    if index <= limit:
        index += 1
        continue

    # if item exists in reference_string
    exists = item in page_frames
    if exists:
        index += 1
        # print(f'{item} is in {page_frames}')
        continue
    else:
        if page_faults == 109:
            print(f'{page_frames}')
        #print(f'{item} is not in {page_frames}')
        index += 1
        tmp = queue.pop(0)
        queue.append(item)
        tmp_index = page_frames.index(item)
        page_frames[tmp_index] = item
        page_faults += 1

    if page_faults == 110:
        print(f'{item} replaced {tmp}: {page_frames}')

print(f'page_faults: {page_faults}')

# # testing if correct page faults
# test_page_faults = 15
# if test_page_faults != page_faults:
#     print(f'{page_faults} != {test_page_faults}')
#
# # correct end state
# test_end_state = [7, 0, 1]
# if test_end_state != page_frames:
#     printf(f'{test_end_state} != {page_frames}')
