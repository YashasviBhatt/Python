num_of_elmnt=int(input('Enter Number of Elements : '))
print('Enter List : ')
initial_list=[int(input()) for lst_ptr in range(0,num_of_elmnt)]
print('Reversed List : ')
for lst_ptr in range(num_of_elmnt-1,-1,-1) :
    print(initial_list[lst_ptr],end=' ')