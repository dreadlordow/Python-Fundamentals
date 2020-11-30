people = int(input())
capacity = int(input())

courses = 0

if people % capacity == 0 :
    courses = int(people / capacity)
    print(courses)
elif people % capacity != 0 :
    full_courses = int(people / capacity + 1)
    print(full_courses)

elif people < capacity :
    print(1)