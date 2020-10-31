#booth encoding
#it used for fastest multiplication
import re
value = input("Enter the value to encode :") + '0'
output = ''
a = re.search(r'[01]*', value)
value = a.group()

for i in range(len(value)-1):
    
    if value[i:i+2] == '11' or value[i:i+2] == '00':
        output += '0'
    elif value[i:i+2] == '10':
        output += '-1'
    elif value[i:i+2] == '01':
        output += '+1'
print(output)
