''' USER CHANGE DATA '''
len_pgframes = 3                        # set amount of frames
desired_page_fault = 110                  # 0 for no pgfaults
parse = 1                               # 1 to parse from data.txt
''' END USER CHANGE DATA '''

def cmp(x, y):
    if x > y:
        return x
    else:
        return y

def search(list, ref, index):
    for i in range(index, len(list)):
        if list[i] == ref:
            return i
    return 999

pgframe = []
foundindex = []
pgfault = 0

if parse == 1:
    text_file = open("data.txt", "r")
    reference_string = text_file.read().split('  ')
    reference_string = list(map(int, reference_string))
else:
    reference_string = [7, 2, 3, 1, 2, 5, 3, 4, 6, 7, 7, 1, 0, 5, 4, 6, 2, 3, 0, 1]

for i in range(len(reference_string)):
    # print(f'pgframe \t {pgframe}\nfoundindex \t {foundindex}')
    if len(pgframe) < len_pgframes:
        pgframe.append(reference_string[i])
        foundindex.append(i)
        pgfault += 1
    elif reference_string[i] in pgframe:
        foundindex[pgframe.index(reference_string[i])] = i
    else:
        searchlist = []
        for j in range(len(pgframe)):
            searchlist.append(search(reference_string, pgframe[j], foundindex[j] + 1))
        # print(f'searchlist \t {searchlist}')
        furthest = cmp(cmp(searchlist[0], searchlist[1]), cmp(searchlist[1], searchlist[2]))
        index = searchlist.index(furthest)
        if pgfault == desired_page_fault - 1:
            print(f'{reference_string[i]} replaces {pgframe[index]}')
            # print(f'{pgframe}')
        pgframe[index] = reference_string[i]
        foundindex[index] = i
        pgfault += 1
        # if pgfault == desired_page_fault:
        #     print(f'{pgframe}')

print(f'pgfault -> {pgfault}')
