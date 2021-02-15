import csv

data = []
with open('file2.csv', 'r') as f:
    file = csv.reader(f)
    for row in file:
        data.append(row)
    
headers = data[0]
star_data = data[1:]

for data in star_data:
    if data[4] != '':
        data[4] = float(data[4]) * 0.102763

for data in star_data:
    if data[3] != '' and data[3] != '40 + 39 +Â\xa0?':
        data[3] = float(data[3]) * 0.000954588

with open('new_file2.csv', 'w') as f2:
    csv_writer = csv.writer(f2)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)