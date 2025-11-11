o = open('sport.txt', mode='r')
lines, sports = [i.split('\t') for i in o.readlines()], {}
for i in lines:
    if i[3].replace(' ', '').split(',') == ['']:  # фильтр испорченных данны, неясным образом оказавшихся в файле
        continue
    for j in (i[3].replace(' ', '').split(',')):
        if j in sports:
            sports[j] += 1
        else:
            sports[j] = 1
print(*sorted(sports.items(), key=lambda item: item[1], reverse=True)[:3])