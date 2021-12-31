structured = open('2021_24_struktur.txt', 'r')
structured = structured.read()
structured = structured.split('\n\n')
newList = []

for item in structured:
    newList.append(item.split('\n'))
transposed = list(zip(*newList))
readable = ''
for i in transposed:
    readable += ','.join(i) + '\n'

print(readable)
