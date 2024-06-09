content = open(r"Bonus_assignment\QuizMark.txt", "r").readlines()
dict1 = {}
list = [(i.split()) for i in content]
for index , value in enumerate(list[0]):
    dict1[value] = []
    for i in list[1:]:
        dict1[value].append(float(i[index]))
open(r"Bonus_assignment\output.txt", "w").write(str(dict1))
