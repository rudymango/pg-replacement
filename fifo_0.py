''' Variables '''
reference_string = []
queue = []
page_frames = [999, 999, 999]
page_frames_length = 3
page_faults = 0

''' Parse Information '''
text_file = open("data.txt", "r")
reference_string = text_file.read().split('  ')
reference_string = list(map(int, reference_string))


''' Initial Queueing '''
index = 0
limit = 2
for item in reference_string:
    queue.append(item)
    index += 1
    page_faults += 1
    if index > limit:
        break

''' FIFO Algorithm '''
page_frames = queue
index = 0
for item in reference_string:
    if index <= limit:
        index += 1
        continue
    exists = item in page_frames
    if exists:
        index += 1
        continue
    else:
        if page_faults == 109:
            print(f'{page_frames}')
        index += 1
        tmp = queue.pop(0)
        queue.append(item)
        tmp_index = page_frames.index(item)
        page_frames[tmp_index] = item
        page_faults += 1
    if page_faults == 110:
        print(f'{item} replaced {tmp}: {page_frames}')

''' Page_Faults Output '''
print(f'page_faults: {page_faults}')
