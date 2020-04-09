# Python program to print text in different color schemes and with different style
# \033[ is Escape code and is always same

class color:
   PURPLE = '\033[95m'                  # python color code for PURPLE color
   CYAN = '\033[96m'                    # python color code for CYAN color
   DARKCYAN = '\033[36m'                # python color code for DARK-CYAN color
   BLUE = '\033[94m'                    # python color code for BLUE color
   GREEN = '\033[92m'                   # python color code for GREEN color
   YELLOW = '\033[93m'                  # python color code for YELLOW color
   RED = '\033[91m'                     # python color code for RED color
   BOLD = '\033[1m'                     # python color code for BOLD
   UNDERLINE = '\033[4m'                # python color code for UNDERLINE
   END = '\033[0m'                      # python color code for NORMAL conversion

print('')
print('THIS IS A NORMAL TEXT')
print(color.PURPLE + 'THIS IS A PURPLE-COLORED TEXT' + color.END)
print(color.CYAN + 'THIS IS A CYAN-COLORED TEXT' + color.END)
print(color.DARKCYAN + 'THIS IS A DARK-CYAN-COLORED TEXT' + color.END)
print(color.BLUE + 'THIS IS A BLUE-COLORED TEXT' + color.END)
print(color.GREEN + 'THIS IS A GREEN-COLORED TEXT' + color.END)
print(color.YELLOW + 'THIS IS A YELLOW-COLORED TEXT' + color.END)
print(color.RED + 'THIS IS A RED-COLORED TEXT' + color.END)
print(color.BOLD + 'THIS IS A BOLD TEXT' + color.END)
print(color.UNDERLINE + 'THIS IS AN UNDERLINED TEXT' + color.END)