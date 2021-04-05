from datetime import datetime,timedelta
now=datetime.now()
dt=datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')

print(dt)
print(now.strftime('%a,%b %d %H:%M'))

print(now + timedelta(hours=10),'-'*40,
now - timedelta(days=1),'-'*40,
now + timedelta(days=2, hours=12),)
