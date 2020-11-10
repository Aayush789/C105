import math
import csv

with open('data.csv', newline= '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

#finding mean 
def mean(data):
    n= len(data)
    total = 0 
    for x in data:
        total += int(x)
    mean = total/n 
    return mean

#squarring and getting the values

squared_list = []
for number in data:
    a = int(number)- mean(data)
    a = a**2
    squared_list.append(a)

#getting sum!

sum = 0
for i in squared_list:
    sum = sum+i 

#dividing the sum by the total value

result = sum/(len(data)-1)

standard_deviation = math.sqrt(result)

print(standard_deviation)