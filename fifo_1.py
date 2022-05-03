''' USER CHANGE DATA '''
len_pgframes = 3                # set amount of frames
parse = 0                       # 1 for parse from data.txt
desired_page_fault = 9          # 0 for no pgfaults
''' END USER CHANGE DATA '''

reference_string = []
queue = []
pgframes = []
pgfaults = 0

if parse == 1:
    text_file = open("data.txt", "r")
    reference_string = text_file.read().split('  ')
    reference_string = list(map(int, reference_string))
else:
    reference_string = [7, 2, 3, 1, 2, 5, 3, 4, 6, 7, 7, 1, 0, 5, 4, 6, 2, 3, 0, 1]

for i in range(len(reference_string)):
    if i < len_pgframes:
        pgfaults += 1
        queue.append(reference_string[i])
        pgframes.append(reference_string[i])
        # print(f'{pgframes} -> {queue} = {pgfaults}')
    elif reference_string[i] in pgframes:
        continue
    else:
        # if pgfaults == desired_page_fault - 1:
        #     print(f'{pgframes}')
        pgfaults += 1
        # print(f'{pgframes} \t {queue} \t {pgfaults}')
        tmp = queue.pop(0)
        queue.append(reference_string[i])
        tmp_index = pgframes.index(tmp)
        pgframes[tmp_index] = reference_string[i]
    if pgfaults == desired_page_fault:
        # print(f'{pgframes}')
        print(f'{reference_string[i]} replaced {tmp}')

print(f'pgfaults -> {pgfaults}')
