import re

string = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Aliquam pellentesque tincidunt nulla id efficitur. 
Vestibulum facilisis accumsan mi, sit amet facilisis urna. 
Etiam nunc neque, maximus sit amet neque non, 
pretium cursus tellus. Nulla malesuada porttitor odio quis tempor. 
Vestibulum orci lectus, egestas sed pharetra tincidunt, mattis ut neque. 
Aliquam vitae tincidunt justo. Suspendisse potenti. 
Nullam at blandit tellus. Aliquam et mi nec justo tincidunt semper. 
Fusce pulvinar tellus viverra metus lacinia, non pulvinar velit malesuada. 
Fusce tempus, mauris eget ultricies feugiat, urna ipsum elementum quam, 
nec convallis ligula lacus at eros. Morbi maximus ac augue at feugiat. 
Maecenas quis imperdiet lorem, et feugiat ex. 
Ut vehicula venenatis ipsum, et aliquet eros tempus nec. 
Sed tempor consectetur risus, rhoncus convallis lorem gravida eu.
'''

# pattern = re.compile('lorem')              # find all the location where 'lorem' is present
# pattern = re.compile('.rem')               # find all the location where 'rem' is present irrespective of substring
# pattern = re.compile('^em')                # find all the location where word starts with 'em'
# pattern = re.compile('em$')                # find all the location where word ends with 'em'
# pattern = re.compile('em*')                # find all the location where word have exactly 1 'e' and zero or more number of 'm'
# pattern = re.compile('em+')                # find all the location where word have exactly 1 'e' and one or more number of 'm'
# pattern = re.compile('em{2}')              # find all the location where word have exactly 1 'e' and exactly 2 number of 'm'
# pattern = re.compile('em|lor')             # find all the location where word have either 'em' or 'lor'
# pattern = re.compile('\Alor')             # find all the location where string have started 'lor'
# pattern = re.compile('\blor')             # find all the location where word have started with 'lor'
# pattern = re.compile('lor\b')             # find all the location where word have ended with 'lor'

pattern = re.compile('lorem')              # find all the location where 'lorem' is present
matches = pattern.finditer(string)

for fndrslt in matches:
    print(fndrslt)




'''
[] A set of characters
\ Signals a special sequence (can also be used to escape special characters)
. Any character (except newline character)
^ Starts with
$ Ends with
* Zero or more occurrences
+ One or more occurrences
{} Exactly the specified number of occurrences
| Either or
() Capture and group

Special Sequences
\A Returns a match if the specified characters are at the beginning of the string
\b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
\d Returns a match where the string contains digits (numbers from 0-9)
\D Returns a match where the string DOES NOT contain digits
\s Returns a match where the string contains a white space character
\S Returns a match where the string DOES NOT contain a white space character
\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
\W Returns a match where the string DOES NOT contain any word characters
\Z Returns a match if the specified characters are at the end of the string
'''