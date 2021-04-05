import csv
dictionaries = [{'age': '30', 'name': 'John', 'last_name': 'Doe'}, {'age': '30', 'name': 'Jane', 'last_name': 'Doe'}]
with open('my.csv', 'w+') as csv_file:
    headers = [k for k in dictionaries[0]]
    print(headers)
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    for dictionary in dictionaries:
        writer.writerow(dictionary)

with open('my.csv', 'r+') as csv_file:
    reader = csv.DictReader(csv_file)
    print(str([row for row in reader]))
