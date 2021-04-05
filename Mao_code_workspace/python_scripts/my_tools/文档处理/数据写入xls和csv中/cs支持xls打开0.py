import csv
with open('123.csv', 'w') as csvfile:
    #spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter = csv.writer(csvfile, dialect='excel')
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])



import csv
with open('123.csv', 'r') as csvfile:
    #spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    spamreader = csv.reader(csvfile, dialect='excel')
    for row in spamreader:
        print (', '.join(row))
