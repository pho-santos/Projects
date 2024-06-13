#https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
import csv

header = ['numbers']
data = [100, 200, 1000, 300]
filename = 'numbers.csv'

with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows([[num]for num in data])

print(f'{csv.reader(filename)}')