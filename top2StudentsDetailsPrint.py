number_of_students = int(input('Enter Number of Students : '))

top_marks_1 = 0
top_marks_2 = 0

top_name_1 = ''
top_name_2 = ''


for detail in range(number_of_students):
    print()
    input_name = input('Enter Name : ')
    input_marks = int(input('Enter Marks : '))
    if input_marks > top_marks_1:
        top_marks_2 = top_marks_1
        top_name_2 = top_name_1
        top_marks_1 = input_marks
        top_name_1 = input_name
    elif input_marks > top_marks_2:
        top_marks_2 = input_marks
        top_name_2 = input_name
    else:
        pass

print('\nTop 2 Students Details are\n\nFirst Student\nName : {}\nMarks : {}\n\nSecond Student\nName : {}\nMarks : {}'.format(
    top_name_1, top_marks_1, top_name_2, top_marks_2))
