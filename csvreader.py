__author__ = 'samhaak'
import csv
count = 0;
with open('C:\Python34\complaints.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar='|')
 for row in data:
  print(', '.join(row))
