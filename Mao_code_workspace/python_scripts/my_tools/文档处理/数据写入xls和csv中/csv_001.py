

# 写

import csv
with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']#列名
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,dialect='excel')

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

# 读
import csv
with open('names.csv','r') as csvfile:
    reader = csv.DictReader(csvfile,dialect='excel')
    for row in reader:
        print(row['first_name'], row['last_name'])
