import math
import re

    #service's name inputted by user
name = str(input("Nom du service : "))
    #transforming service's name in binary
binary_name = ' '.join(format(ord(c), 'b') for c in name)
print("Nom en binaire : ", binary_name)
    #defining the number of the wanted service to 0
num_service = int(0)
    #define list with the number of 1 contained in 'binary_name'
x = re.findall('[1]', binary_name)
    #defines how much 1 are in the list
y = len(x)
    #set port number as 'number of 1' * 100
port_number = y*100
print('Le port devrait être le', port_number)