import smtplib
my_address = 'mjt1220@126.com'
hears = [ 'Subject: A test',
      'From: ' + my_address,
      'To: ' + my_address,
      ]
entries = "Hello"
msg ='r\n'.join(hears) + 'r\n' + ' '.join(entries)
smtp = smtplib.SMTP('smtp.126.com',587)
smtp.starttls('smtp.126.com')
smtp.sendmail(my_address, [my_address] , msg)
smtp.close()
