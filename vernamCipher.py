# Function Vernam Cipher
# Created by Yashasvi Bhatt

def VernamCipher(input_message, one_time_pad):
    output = ''
    if len(input_message) == len(one_time_pad):
        for i,o in zip(input_message, one_time_pad):
            if i == ' ' and o == ' ':
                output += ' '
                continue
            elif i == ' ' and o != ' ' or i != ' ' and o == ' ':
                print('Invalid Inputs')
                break
            a = ord(i) + ord(o)                         # ord is used to find the ascii value of a character
            if a > 219:
                a = a - 123
                output += chr(a)                        # chr is used to fetch the character from its ascii value
            else:
                output += chr(a - 97)
        return output
    else:
        print("Length of PT and OTP must be same")

input_message=input("Enter Plain Text : ")
one_time_pad=input("Enter One Time Pad : ")

print("Cipher Text : ", VernamCipher(input_message, one_time_pad))