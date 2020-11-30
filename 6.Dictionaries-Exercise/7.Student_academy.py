n = int(input())

grades_dict = {}

for _ in range(n):
    name = input()
    grade = float(input())
    if name not in grades_dict:
        grades_dict[name] =[]
    grades_dict[name].append(grade)

for name, score in grades_dict.items():
    avg_score = sum(score)/len(score)
    grades_dict[name] = avg_score
grades_dict = {key:value for key,value in grades_dict.items() if value >= 4.5}
grades_dict = dict(sorted(grades_dict.items(), key=lambda n: n[1],reverse=True))

for k,v in grades_dict.items():
    print(f'{k} -> {v:.2f}')
