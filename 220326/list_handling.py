def file_reader(dic: dict, file: str):
    with open(file) as file:
        lines_1 = [line.strip() for line in file]

    for l in lines_1:
        try:
            dic[l] += 1
        except KeyError:
            dic[l] = 1


dic = {}
files = ['./txt/file1.txt', './txt/file2.txt']
for file in files:
    file_reader(dic, file)

result = []
for k, v in dic.items():
    if v >= 2:
        result.append(k)

print(result)
