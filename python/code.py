import math
import re

name = str(input("Nom du service : "))

binary_name = ' '.join(format(ord(c), 'b') for c in name)
print("Nom en binaire : ", binary_name)

num_service = int(0)

#search using regex
x = re.findall('[1]', binary_name)
print(x)

print(len(x))