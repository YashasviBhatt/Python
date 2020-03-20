# Program for Rotation of list by a Rotation Factor

input_list=list(map(int, input('Enter List\n').split()))
rotation_factor=int(input('Enter Rotation Factor : '))
if rotation_factor > len(input_list):
    print('Invalid Value Entered')
    exit()
rotated_list=[]

for lst_ptr in range(len(input_list)-1, len(input_list)-rotation_factor-1, -1):
    rotated_list.append(input_list[lst_ptr])
for lst_ptr in range(len(input_list)-rotation_factor):
    rotated_list.append(input_list[lst_ptr])

print(rotated_list)