def ListReversal(input_list) :
    num_of_elmnts=len(input_list)
    reversed_list=[]
    for initial_ptr,rev_ptr in zip(range(0,num_of_elmnts),range(num_of_elmnts-1,-1,-1)) :
        reversed_list.append(input_list[rev_ptr])
    return reversed_list

def ListInput(input_list,num_of_elmnts) :
    if num_of_elmnts < 0 :
        print('Invalid Number Entered')
    elif num_of_elmnts == 0 :
        print('Empty List can\'t be Reversed')
    else :
        return [int(input()) for inpt_elmnt in range(0,num_of_elmnts)]

num_of_elmnts=int(input('Enter Number of Elements : '))
input_list=[]

print('Enter List')

input_list=ListInput(input_list,num_of_elmnts)
reversed_list=ListReversal(input_list)

print('Reversed List : {}'.format(reversed_list))