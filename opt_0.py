''' Variables '''
reference_string = []
pgframe = []
foundindex = []
length = 3

''' Parse Information '''
text_file = open("data.txt", "r")
reference_string = text_file.read().split('  ')
reference_string = list(map(int, reference_string))

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

pgfault = 0

for i in range(len(reference_string)):
    # print(f'pgframe \t {pgframe}\nfoundindex \t {foundindex}')
    if len(pgframe) < length:
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
        if pgfault == 109:
            print(f'{reference_string[i]} replaces {pgframe[index]}')
            print(f'{pgframe}')
        pgframe[index] = reference_string[i]
        foundindex[index] = i
        pgfault += 1
        if pgfault == 110:
            print(f'{pgframe}')

print(f'pgfault -> {pgfault}')
