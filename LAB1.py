import requests

lines, sports = [i.split('\t') for i in requests.get('https://dfedorov.spb.ru/python3/sport.txt').content.decode('cp1251').split('\n')], {}
for i in lines:
    if i == ['']:
        continue
for i in lines:
    if i[3].replace(' ', '').split(',') == ['']:  # фильтр испорченных данны, неясным образом оказавшихся в файле
        continue
    for j in (i[3].replace(' ', '').split(',')):
        if j in sports:
            sports[j] += 1
        else:
            sports[j] = 1

print(*sorted(sports.items(), key=lambda item: item[1], reverse=True)[:3])
