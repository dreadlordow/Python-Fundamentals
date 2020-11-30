course_dict = {}

line = input()

while line != 'end':
    course, student_name = line.split(' : ')
    if course not in course_dict:
        course_dict[course] = []
    course_dict[course].append(student_name)

    line = input()
sorted_dict = dict(sorted(course_dict.items(), key=lambda x:len(x[1]),reverse=True))

for key,sorted_value in sorted_dict.items():
    sorted_dict[key] = sorted(sorted_value)

for course,students in sorted_dict.items():
    print(f'{course}: {len(students)}')
    for student in students:
        print(f'-- {student}')

