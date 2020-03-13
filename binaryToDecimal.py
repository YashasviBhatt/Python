# Program to find the decimal equivalent of n digit binary number

def BinaryToDecimal(bin_num,bin_len):
    # creating a list enlisted with binary codes of decimal numbers
    binary_input_list = ["{:b}".format(num) for num in range(0,2**bin_len)]
    multiplier=1
    dec_eqvlnt=0

    # checking that the input binary number should contain max 4 digits
    if len(str(bin_num)) > bin_len :
        print('Binary Number Inserted Should be of 4 digits maximum')
        exit()
    # checking whether the entered binary os valid or not

    flag=0
    for num in binary_input_list :
        if str(bin_num)==num :
            flag=1
    if flag==0 :
        print('Invalid Binary Entered')
        exit()
    # calculating the binary equivalent

    else :
        while bin_num>=1 :
            dec_eqvlnt+=int(bin_num%10*multiplier)
            bin_num=int(bin_num/10)
            multiplier*=2

        return dec_eqvlnt

binary_input=int(input('Enter a Binary Number : '))
bin_len=len(str(binary_input))
# ensuring that the inserted binary should not be greater than 10
# since it will be so much heavy for program
if bin_len>10 :
    print('Value too Large (insert value less than or equals to of length 10)')
    exit()


# calling the BinaryToDecimal function that returns a value to a variable
binary_eqvlnt=BinaryToDecimal(binary_input,bin_len)
print('The Binary Equivalent of {} is {}'.format(binary_input,binary_eqvlnt))

# or directly you can use bin function in python which will return bin equivalent of number
# a=int(input('Enter Binary'))
# print(bin(a))  // it will return binary with 0b at the starting
# print({:b}.format(a))   // it will return binary without 0b at starting
