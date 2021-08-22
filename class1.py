import csv
import pandas as pd
import plotly.express as px
with open('class1.csv', newline="") as f:
  reader = csv.reader(f)
  file_data = list(reader)
file_data.pop(0)

sum = 0
n = len(file_data)

for marks in file_data:
  sum += float(marks[1])

mean = sum/n

print('Average marks of all students in the class: ' + str(mean))

datasheet = pd.read_csv('class1.csv')
figure = px.scatter(datasheet, x='Student Number', y='Marks')
figure.update_layout(shapes=[
  dict(type='line', y0=mean, y1=mean, x0=0, x1=n)
])
figure.update_yaxes(rangemode="tozero")

figure.show()