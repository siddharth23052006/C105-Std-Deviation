import csv
import math

with open('data.csv', newline="") as f:
  reader = csv.reader(f)
  file_data = list(reader)

data = file_data[0]

def mean(data):
  n = len(data)
  total = 0
  for x in data:
    total += int(x)
  
  mean = total/n
  return mean

squaredList = []
for num in data:
  a = int(num) - mean(data)
  a = a**2
  squaredList.append(a)

sumUp = 0
for i in squaredList:
  sumUp = sumUp + i

result = sumUp/len(data)

stdDeviation = math.sqrt(result)

print(stdDeviation)
print(mean(data))